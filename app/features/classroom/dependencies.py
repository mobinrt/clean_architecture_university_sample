from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.db.database import db

from app.features.classroom.data.repository.classroom_repo_imp import ClassroomRepositoryImp
from app.features.classroom.data.repository.classroom_unit_of_work_imp import ClassroomUnitOfWorkImp
from app.features.classroom.data.services.classroom_service_imp import ClassroomServiceImp
from app.features.classroom.domain.repository.classroom_repo import ClassroomRepository
from app.features.classroom.domain.repository.classroom_unite_of_work import ClassroomUnitOfWork
from app.features.classroom.domain.services.classroom_service import ClassroomService
from app.features.classroom.domain.usecase.create_classroom import CreateClassroomUseCase, CreateClassroomUseCaseImp
from app.features.classroom.domain.usecase.get_classroom import GetClassroomUsecase, GetClassroomUsecaseImp
from app.features.classroom.domain.usecase.get_classrooms import GetClassroomsUsecase, GetClassroomsUsecaseImp
#from app.features.classroom.domain.usecase.update_classroom import UpdateclassroomUsecase, UpdateclassroomUsecaseImp
from app.features.classroom.domain.usecase.delete_classroom import DeleteClassroomUseCase, DeleteClassroomUseCaseImpl

async def get_classroom_repository(session: Session = Depends(db.get_session)) -> ClassroomRepository:
    return ClassroomRepositoryImp(session)

async def get_classroom_serivce(session: Session = Depends(db.get_session)) -> ClassroomService:
    return ClassroomServiceImp(session)

async def get_classroom_unit_of_work(
    session: Session = Depends(db.get_session),
    classroom_repository: ClassroomRepository = Depends(get_classroom_repository),
) -> ClassroomUnitOfWork:
    return ClassroomUnitOfWorkImp(session, classroom_repository)

async def get_create_classroom_use_case(
    unit_of_work: ClassroomUnitOfWork = Depends(get_classroom_unit_of_work),
) -> CreateClassroomUseCase:
    return CreateClassroomUseCaseImp(unit_of_work)

async def get_classroom_use_case(classroom_service: ClassroomService = Depends(get_classroom_serivce)) -> GetClassroomUsecase:
    return GetClassroomUsecaseImp(classroom_service)

async def get_classrooms_use_case(classroom_service: ClassroomService = Depends(get_classroom_serivce)) -> GetClassroomsUsecase:
    return GetClassroomsUsecaseImp(classroom_service)
 
async def get_delete_classroom_use_case(
    unit_of_work: ClassroomUnitOfWork = Depends(get_classroom_unit_of_work),
) -> DeleteClassroomUseCase:
    return DeleteClassroomUseCaseImpl(unit_of_work)

'''
def get_update_classroom_use_case(unit_of_work: ClassroomUnitOfWork = Depends(get_classroom_unit_of_work)) -> UpdateClassroomUsecase:
    return UpdateClassroomUsecaseImp(unit_of_work)
'''