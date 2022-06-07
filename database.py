import motor.motor_asyncio

Mongo_Detail = 

client = motor.motor_asyncio.AsyncIOMotorClient(Mongo_Detail)
database = client.Student_info


student_collection = database.get_collection("students_collection")
users_collection = database.get_collection("users_collection")



def student_helper(student) -> dict:
    return {
        "student_name": student["student_name"],
        "student_class": student["student_class"],
        "student_session": student["student_session"],
        "address": student["address"]
    }

def student_helper_with_id(student) -> dict:
    return {
        "_id" : str(student["_id"]),
        "student_name": student["student_name"],
        "student_class": student["student_class"],
        "student_session": student["student_session"],
        "address": student["address"]
    }

