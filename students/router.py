from fastapi import APIRouter, HTTPException

from .storage import STUDENTS
from .schema import StudentCreateSchema, Student

router = APIRouter()


@router.post("/")
async def create_item(student: StudentCreateSchema):
    s = Student(first_name=student.first_name, last_name=student.last_name, student_id=len(STUDENTS)+1)
    STUDENTS[s.student_id] = s
    return s


@router.get("/")
async def read_item():
    return STUDENTS


@router.put("/")
async def update_idem(student_id: int, first_name: str, last_name: str):
    if student_id not in STUDENTS:
        raise HTTPException(
            status_code=404,
            detail="Student not found",
        )

    else:
        student = STUDENTS[student_id]
        student.first_name = first_name
        student.last_name = last_name

    return student

# @router.post("/{student_id}/marks/{ocena}")
# async def add_mark(student_id: int):