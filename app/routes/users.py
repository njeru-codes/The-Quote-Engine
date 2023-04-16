from fastapi import APIRouter, HTTPException, status , Depends
from .. import schemas
from ..config import db_connection
from datetime import datetime
from ..auth import passlib, apikey
from pymongo.errors import DuplicateKeyError
from ..auth import auth
from bson.objectid import ObjectId


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
        raise HTTPException( status_code=500, detail=f'internal server error')
    finally:
        db_conn.close()
    return{
        "user_id": str(new_user),
        "email": user['email'],
    }

@router.post('/password/change_password', status_code=200)
async def change_password(password:schemas.NewPassword,  current_user: str = Depends(auth.get_current_user), db_conn=Depends(db_connection) ):
    db_users = db_conn['db_quotes']['users']
    user = db_users.find_one({'_id': ObjectId(current_user) })
    if password.new_password == password.confirm_password:
        user['password'] = passlib.get_password_hash(password.new_password)
        return
     
