from bson.objectid import ObjectId

from ..database import (
database,users_collection
)

from .. models.user import (
    UserSchema,
    UserLoginSchema
) 

async def add_user(student_data: dict) -> dict:
    student = await users_collection.insert_one(student_data)
    return "created"

async def check_user(data: UserLoginSchema) -> bool:
    async for user in users_collection.find():
        if user.email == data.email and user.password == data.password:
            return True
    return False
