from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.db.database import db
from app.core.util.id_manager import UniqueID, get_unique_id_instance

from app.features.teacher.data.model import TeacherModel
from app.features.teacher.data.repository.teacher_repo_imp import TeacherRepositoryImp
from app.features.teacher.data.repository.teacher_unit_of_work_imp import TeacherUnitOfWorkImp
from app.features.teacher.data.services.teacher_service_imp import TeacherServiceImp
from app.features.teacher.domain.repository.teacher_repo import TeacherRepository
from app.features.teacher.domain.repository.teacher_unit_of_work import TeacherUnitOfWork
from app.features.teacher.domain.services.teacher_service import TeacherService
from app.features.teacher.domain.usecase.create_teacher import CreateTeacherUseCase, CreateTeacherUseCaseImp
from app.features.teacher.domain.usecase.get_teacher import GetTeacherUsecase, GetTeacherUsecaseImp
from app.features.teacher.domain.usecase.get_teachers import GetTeachersUsecase, GetTeachersUsecaseImp
from app.features.teacher.domain.usecase.update_teacher import UpdateTeacherUseCase, UpdateTeacherUseCaseImp
from app.features.teacher.domain.usecase.delete_teacher import DeleteTeacherUseCase, DeleteTeacherUseCaseImpl
from app.features.teacher.domain.usecase.hash_table_teacher import GetHashTableForTeacherUseCase, GetHashTableForTeacherUseCaseImp
from app.features.teacher.domain.auth.auth_teacher import TeacherAuthService


async def get_teacher_repository(session: Session = Depends(db.get_session)) -> TeacherRepository:
    return TeacherRepositoryImp(session)


async def get_teacher_serivce(session: Session = Depends(db.get_session)) -> TeacherService:
    return TeacherServiceImp(session)


async def get_auth_service(session: Session = Depends(db.get_session)) -> TeacherAuthService:
    return TeacherAuthService(session, TeacherModel)


async def get_teacher_unit_of_work(
    session: Session = Depends(db.get_session),
    teacher_repository: TeacherRepository = Depends(get_teacher_repository),
    teacher_service: TeacherService = Depends(get_teacher_serivce)
) -> TeacherUnitOfWork:
    return TeacherUnitOfWorkImp(session, teacher_repository, teacher_service)


async def get_create_teacher_use_case(
    unit_of_work: TeacherUnitOfWork = Depends(get_teacher_unit_of_work),
    unique_id: UniqueID = Depends(get_unique_id_instance)
) -> CreateTeacherUseCase:
    return CreateTeacherUseCaseImp(unit_of_work, unique_id)


async def get_teacher_use_case(uow: TeacherUnitOfWork = Depends(get_teacher_unit_of_work)) -> GetTeacherUsecase:
    return GetTeacherUsecaseImp(uow)


def get_teachers_use_case(uow: TeacherUnitOfWork = Depends(get_teacher_unit_of_work)) -> GetTeachersUsecase:
    return GetTeachersUsecaseImp(uow)
 
 
def get_delete_teacher_use_case(
    unit_of_work: TeacherUnitOfWork = Depends(get_teacher_unit_of_work),
    unique_id: UniqueID = Depends(get_unique_id_instance)
) -> DeleteTeacherUseCase:
    return DeleteTeacherUseCaseImpl(unit_of_work, unique_id)


async def get_hash_table_use_case(
    unique_id: UniqueID = Depends(get_unique_id_instance),
    ) -> GetHashTableForTeacherUseCase:
    return GetHashTableForTeacherUseCaseImp(unique_id)


def get_update_teacher_use_case(
    unit_of_work: TeacherUnitOfWork = Depends(get_teacher_unit_of_work),
    auth: TeacherAuthService = Depends(get_auth_service),
    unique_id: UniqueID = Depends(get_unique_id_instance)
    ) -> UpdateTeacherUseCase:
    return UpdateTeacherUseCaseImp(unit_of_work, auth, unique_id)
