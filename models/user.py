from pydantic import BaseModel, Field, EmailStr


class UserSchema(BaseModel):
    user_name : str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "user_name": "jon johny janardharan",
                "email": "john@x.com",
                "password": "weakpassword"
            }
        }

class UserLoginSchema(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "email": "john@x.com",
                "password": "weakpassword"
            }
        }
