from fastapi import APIRouter

from .create_student_router import router as create_student_router
from .get_student_router import router as get_student_router
from .get_students_router import router as get_students_router
from .delete_student_router import router as delete_student_router
student_router = APIRouter()

student_router.include_router(create_student_router)
student_router.include_router(get_student_router)
student_router.include_router(get_students_router)
student_router.include_router(delete_student_router)
 