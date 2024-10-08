from fastapi import APIRouter

from .create_classroom_router import router as create_classroom_router
from .get_classroom_router import router as get_classroom_router
from .get_classrooms_router import router as get_classrooms_router
from .delete_classroom_router import router as delete_classroom_router

classroom_router = APIRouter()

classroom_router.include_router(create_classroom_router)
classroom_router.include_router(get_classroom_router)
classroom_router.include_router(get_classrooms_router)
classroom_router.include_router(delete_classroom_router)
