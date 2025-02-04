from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type:str
    
class TokenData(BaseModel):
    username: str | None = None
    
class SignUpUser(BaseModel):
    username: str
    email: str
    password: str
    full_name: str | None = None
    
class LoginUser(BaseModel):
    username: str | None = None
    email: str 
    password: str