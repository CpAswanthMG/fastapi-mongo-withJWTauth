from bson.objectid import ObjectId

from ..database import (
database,student_collection,
student_helper,
student_helper_with_id
)

async def retrieve_students():
    students_list = []
    async for student in student_collection.find().limit(5):
        students_list.append(student_helper_with_id(student))
    return students_list


async def add_student(student_data: dict) -> dict:
    new_student_request = student_helper(student_data)
    student = await student_collection.insert_one(new_student_request)
    return "created"

async def retrieve_student_by_id(id:str) -> dict:
    student = await student_collection.find_one({"_id":ObjectId(id)})
    student_details = student_helper_with_id(student)
    return student_details
    
# Update a student with a matching ID
async def update_student(id: str, data: dict):
    student = await student_collection.find_one({"_id":ObjectId(id)})
    student_data = student_helper(data)
    if student:
        updated_student = await student_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": student_data}
        )
    return "updated"


async def delete_student(id: str):
    student = await student_collection.find_one({"_id":ObjectId(id)})
    if student:
        await student_collection.delete_one(
            {"_id": ObjectId(id)}
        )
        return True
    