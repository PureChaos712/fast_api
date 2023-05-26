from fastapi import FastAPI
from pydantic import BaseModel


class StudentCreateSchema(BaseModel):
    first_name: str
    last_name: str


class StudentUpdateSchema(BaseModel):
    first_name: str
    last_name: str


class Student(BaseModel):
    student_id: int
    first_name: str
    last_name: str


app = FastAPI()
STUDENTS = {}


@app.post("/student/")
async def create_item(student: StudentCreateSchema):
    s = Student(first_name=student.first_name, last_name=student.last_name, student_id=len(STUDENTS)+1)
    STUDENTS[s.student_id] = s
    return s


@app.get("/students")
async def read_item():
    return STUDENTS


