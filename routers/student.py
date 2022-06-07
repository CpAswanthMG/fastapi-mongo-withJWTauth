from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Body, Depends
from ..auth.auth_bearer import JWTBearer


from  ..crud.student import (
    add_student,
    retrieve_students,
    retrieve_student_by_id,
    update_student,
    delete_student
)

from .. models.student import (
    CreateStudent,
    StudentList,
    ResponseModel,
    ErrorResponseModel,
)

router = APIRouter()

@router.post("/",dependencies=[Depends(JWTBearer())], response_description ="student data added into database")
async def add_student_data(student: CreateStudent = Body(...)):
    student_data = jsonable_encoder(student)
    new_student = await add_student(student_data)
    return ResponseModel(new_student,201,"created")


@router.get("/",response_description="Students data Retrieved")
async def get_student():
    student_list = await retrieve_students()
    if student_list:
        return ResponseModel(student_list,200,"student data retrieved")
    return ResponseModel(student_list,204,"Empty list returned")


@router.get("/{id}", response_description="Student data retrieved")
async def get_student_data(id):
    student = await retrieve_student_by_id(id)
    if student:
        return ResponseModel(student,200, "Student data retrieved successfully")
    return ErrorResponseModel("An error occurred.",204, "Student doesn't exist.")


@router.put("/{id}",dependencies=[Depends(JWTBearer())])
async def update_student_data(id: str,
    data:CreateStudent = Body(..., embed=True),
    ):
    update_request = {k: v for k, v in data.dict().items() if v is not None}
    updated_students = await update_student(id,update_request)
    if updated_students:
        return ResponseModel(
            f"Student with ID: {id} update is successful",
            202,
            "Student name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the student data.",
    )


@router.delete("/{id}", dependencies=[Depends(JWTBearer())],response_description="Student data deleted from the database")
async def delete_student_data(id: str):
    deleted_student = await delete_student(id)
    if deleted_student:
        return ResponseModel(
            "Student with ID: {} removed".format(id),204, "Student deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Student with id {0} doesn't exist".format(id)
    )

