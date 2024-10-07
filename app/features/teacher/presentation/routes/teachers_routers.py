from fastapi import APIRouter

from .create_teacher_router import router as create_teacher_router
from .get_teacher_router import router as get_teacher_router
from .get_teachers_router import router as get_teachers_router
from .delete_teacher_router import router as delete_teacher_router
from .get_hash_table_teahcer_router import router as get_hash_table_teahcer_router

teacher_router = APIRouter()

teacher_router.include_router(create_teacher_router)
teacher_router.include_router(get_teacher_router)
teacher_router.include_router(get_teachers_router)
teacher_router.include_router(delete_teacher_router)
teacher_router.include_router(get_hash_table_teahcer_router)
