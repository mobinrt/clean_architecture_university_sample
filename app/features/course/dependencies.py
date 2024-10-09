from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.db.database import db
from app.core.util.id_manager import UniqueID, get_unique_id_instance
from app.features.course.data.repository.course_repo_imp import CourseRepositoryImp
from app.features.course.data.repository.course_unit_of_work_imp import CourseUnitOfWorkImp
from app.features.course.data.services.course_service_imp import CourseServiceImp
from app.features.course.domain.repository.course_repo import CourseRepository
from app.features.course.domain.repository.course_unit_of_work import CourseUnitOfWork
from app.features.course.domain.services.course_service import CourseService
from app.features.course.domain.usecase.create_course import CreateCourseUseCase, CreateCourseUseCaseImp
from app.features.course.domain.usecase.get_course import GetCourseUsecase, GetCourseUsecaseImp
from app.features.course.domain.usecase.get_courses import GetCoursesUsecase, GetCoursesUsecaseImp
from app.features.course.domain.usecase.hash_table_course import GetHashTableForCourseUseCase, GetHashTableForCourseUseCaseImp
#from app.features.course.domain.usecase.update_course import UpdateCourseUsecase, UpdateCourseUsecaseImp
from app.features.course.domain.usecase.delete_course import DeleteCourseUseCase, DeleteCourseUseCaseImpl

async def get_course_repository(session: Session = Depends(db.get_session)) -> CourseRepository:
    return CourseRepositoryImp(session)

async def get_course_service(session: Session = Depends(db.get_session)) -> CourseService:
    return CourseServiceImp(session)

async def get_course_unit_of_work(
    session: Session = Depends(db.get_session),
    course_repository: CourseRepository = Depends(get_course_repository),
    course_service: CourseService = Depends(get_course_service),
) -> CourseUnitOfWork:
    return CourseUnitOfWorkImp(session, course_repository, course_service)

async def get_create_course_use_case(
    unit_of_work: CourseUnitOfWork = Depends(get_course_unit_of_work),
    unique_id: UniqueID = Depends(get_unique_id_instance)
) -> CreateCourseUseCase:
    return CreateCourseUseCaseImp(unit_of_work, unique_id)

async def get_course_use_case(uow: CourseUnitOfWork = Depends(get_course_unit_of_work)) -> GetCourseUsecase:
    return GetCourseUsecaseImp(uow)

async def get_courses_use_case(uow: CourseUnitOfWork = Depends(get_course_unit_of_work)) -> GetCoursesUsecase:
    return GetCoursesUsecaseImp(uow)

async def get_delete_course_use_case(
    unit_of_work: CourseUnitOfWork = Depends(get_course_unit_of_work),
    unique_id: UniqueID = Depends(get_unique_id_instance)
) -> DeleteCourseUseCase:
    return DeleteCourseUseCaseImpl(unit_of_work, unique_id)

async def get_hash_table_use_case(
    unique_id: UniqueID = Depends(get_unique_id_instance),
    ) -> GetHashTableForCourseUseCase:
    return GetHashTableForCourseUseCaseImp(unique_id)

'''
def get_update_course_use_case(unit_of_work: CourseUnitOfWork = Depends(get_course_unit_of_work)) -> UpdateCourseUsecase:
    return UpdateCourseUsecaseImp(unit_of_work)
'''
