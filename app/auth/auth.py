from fastapi import  HTTPException, status, Depends
from fastapi.security import APIKeyHeader, OAuth2PasswordBearer
from ..config import db_connection, settings
from jose import JWTError, jwt
from datetime import datetime, timedelta

api_key_header = APIKeyHeader(name="X-API-Key")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

async def validate_api_key(api_key:str = Depends(api_key_header)):
    try:
        db_conn = db_connection()
        users = db_conn.db_quotes.users
        db_key = users.find_one( {'apikey':api_key} )
        if db_key is None:
            raise HTTPException( status_code=status.HTTP_400_BAD_REQUEST, detail='invalid api key')
    except Exception as error:
        print(error)
        raise HTTPException(status_code=401, detail="could not valiadate API key")
    finally:
        db_conn.close()
    return api_key


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)
    return encoded_jwt



def verify_access_token(token: str, credentials_exception):
    try:
        payload =jwt.decode(token, settings.secret_key )
        user_id:str = payload.get("user_id")
        if id is None: 
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    return user_id

def get_current_user(token :str=Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code= status.HTTP_401_UNAUTHORIZED,
        detail= "could not validate credentials", 
        headers={"WWW-Authenticate": "Bearer "
    })
    return verify_access_token(token, credentials_exception)