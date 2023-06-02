from functools import lru_cache

from .schema import Student, Mark

STUDENTS: dict[int, Student] = {}
MARKS: dict[int, list[Mark]] = {}


@lru_cache(maxsize=1)
def get_students_storage() -> dict[int, Student]:
    return STUDENTS


def get_marks() -> dict[int, list[Mark]]:
    return MARKS
