from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class Quote(BaseModel):
    quote: str
    author: Optional[str]=None


class NewUser(BaseModel):
    email: EmailStr
    password: str
    first_name: str
    surname: str
    username:str

class User(BaseModel):
    identity: str
    password: str

