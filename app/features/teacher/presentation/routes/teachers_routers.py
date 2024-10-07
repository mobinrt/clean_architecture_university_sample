from fastapi import APIRouter

from .create_teacher_router import router as create_student_router
from .get_teacher_router import router as get_student_router
from .get_teachers_router import router as get_students_router
from .delete_teacher_router import router as delete_student_router
student_router = APIRouter()

student_router.include_router(create_student_router)
student_router.include_router(get_student_router)
student_router.include_router(get_students_router)
student_router.include_router(delete_student_router)
 