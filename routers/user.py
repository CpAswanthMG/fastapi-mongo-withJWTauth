from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Body, Depends
from .. auth.auth_bearer import JWTBearer
from .. auth.auth_handler import signJWT

from .. models.user import (
    UserSchema,
    UserLoginSchema
) 
from .. crud.user import (
    add_user,
    check_user
)
router = APIRouter()

@router.post("/signup", response_description ="User data added into database")
async def create_user(user: UserSchema = Body(...)):
    user_data = jsonable_encoder(user)
    await add_user(user_data)
    return signJWT(user.email)

@router.post("/login")
def user_login(user: UserLoginSchema = Body(...)):
    if check_user(user):
        return signJWT(user.email)
    return {
        "error": "Wrong login details!"
}