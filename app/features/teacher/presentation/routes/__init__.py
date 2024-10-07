from fastapi import APIRouter

router = APIRouter(
    prefix='/students',
    tags=['student'],
)