from pydantic import BaseModel
from typing import Optional,List



class StudentBaseModel(BaseModel):
    student_name : str 
    student_class : int 
    student_session : str
    
class AddressBaseModel(BaseModel):
    address_line1 : str
    address_line2 : str 
    city : str 
    pin : int 


class CreateStudent(StudentBaseModel):
    address : List[AddressBaseModel]


class StudentList(CreateStudent):
    id : int



def ResponseModel(data,code,message):
    return{
        "data": data, "code": code,
        "message": message
    }

def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}