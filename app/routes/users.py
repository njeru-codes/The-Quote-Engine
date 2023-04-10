from fastapi import APIRouter, HTTPException, status , WebSocket
from .. import schemas
from ..config import db_connection
from datetime import datetime
from ..auth import passlib, apikey
from pymongo.errors import DuplicateKeyError


router = APIRouter(
    prefix='/users'
)


@router.post('/new')
async def new_user(user: schemas.NewUser):
    db_conn = db_connection()
    try:
        db_users = db_conn.db_quotes.users
        user.password = passlib.get_password_hash( user.password )
        user = user.dict()
        user['apikey']= apikey.create_api_key()
        user['created_at'] = datetime.now()
        
        new_user = db_users.insert_one(user).inserted_id
    except DuplicateKeyError as error:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail= f'{error}')
    except Exception as error:
        print(error)
    finally:
        db_conn.close()
    return{
        "user_id": str(new_user),
        "email": user['email'],
    }
