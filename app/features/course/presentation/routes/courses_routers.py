from fastapi import APIRouter

from .create_course_router import router as create_course_router
from .get_course_router import router as get_course_router
from .get_courses_router import router as get_courses_router
from .delete_course_router import router as delete_course_router
from .get_hash_table_course_router import router as get_hash_table_course_router

course_router = APIRouter()

course_router.include_router(create_course_router)
course_router.include_router(get_course_router)
course_router.include_router(get_courses_router)
course_router.include_router(delete_course_router)
course_router.include_router(get_hash_table_course_router)
