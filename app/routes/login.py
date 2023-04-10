from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from .. import schemas
from ..config import db_connection
from ..auth import passlib ,auth

router = APIRouter(
    prefix='/login'
)

@router.post('', status_code=status.HTTP_200_OK)
async def login( user:OAuth2PasswordRequestForm=Depends()):
    db_users = db_connection()['db_quotes']['users']
    db_user = db_users.find_one({ '$or': [ { 'username': user.username}, { 'email': user.username } ] })
    if not db_user:
        raise HTTPException(status_code=400, detail='Invalid credentials')
    else:
        if not passlib.verify_password(user.password, db_user['password']):
            raise HTTPException(status_code=400, detail='Invalid credentials')
        data ={ 'user_id': str(db_user['_id'])}
        return{
            'access_token': auth.create_access_token(data),
            'token_type': 'Bearer'
        }



@router.get('/protected')
async def protected_route(current_user: str = Depends(auth.get_current_user)):
    return {"user_id": current_user}


