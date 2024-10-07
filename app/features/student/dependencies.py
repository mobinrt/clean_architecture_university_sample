from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.db.database import db
from app.core.util.id_manager import UniqueID, get_unique_id_instance
from app.features.student.data.repository.student_repo_imp import StudentRepositoryImp
from app.features.student.data.repository.student_unit_of_work_imp import StudentUnitOfWorkImp
from app.features.student.data.services.student_service_imp import StudentServiceImp
from app.features.student.domain.repository.student_repo import StudentRepository
from app.features.student.domain.repository.student_unite_of_work import StudentUnitOfWork
from app.features.student.domain.services.student_service import StudentService
from app.features.student.domain.usecase.create_student import CreateStudentUseCase, CreateStudentUseCaseImp
from app.features.student.domain.usecase.get_student import GetStudentUsecase, GetStudentUsecaseImp
from app.features.student.domain.usecase.get_students import GetStudentsUsecase, GetStudentsUsecaseImp
from app.features.student.domain.usecase.hash_table_student import GetHashTableForStudentUseCase, GetHashTableForStudentUseCaseImp
#from app.features.student.domain.usecase.update_student import UpdateStudentUsecase, UpdateStudentUsecaseImp
from app.features.student.domain.usecase.delete_student import DeleteStudentUseCase, DeleteStudentUseCaseImpl

async def get_student_repository(session: Session = Depends(db.get_session)) -> StudentRepository:
    return StudentRepositoryImp(session)

async def get_student_serivce(session: Session = Depends(db.get_session)) -> StudentService:
    return StudentServiceImp(session)

async def get_student_unit_of_work(
    session: Session = Depends(db.get_session),
    student_repository: StudentRepository = Depends(get_student_repository),
) -> StudentUnitOfWork:
    return StudentUnitOfWorkImp(session, student_repository)

async def get_create_student_use_case(
    unit_of_work: StudentUnitOfWork = Depends(get_student_unit_of_work),
    unique_id: UniqueID = Depends(get_unique_id_instance)
) -> CreateStudentUseCase:
    return CreateStudentUseCaseImp(unit_of_work, unique_id)

async def get_student_use_case(student_service: StudentService = Depends(get_student_serivce)) -> GetStudentUsecase:
    return GetStudentUsecaseImp(student_service)

def get_students_use_case(student_service: StudentService = Depends(get_student_serivce)) -> GetStudentsUsecase:
    return GetStudentsUsecaseImp(student_service)
 
def get_delete_student_use_case(
    unit_of_work: StudentUnitOfWork = Depends(get_student_unit_of_work),
    unique_id: UniqueID = Depends(get_unique_id_instance)
) -> DeleteStudentUseCase:
    return DeleteStudentUseCaseImpl(unit_of_work, unique_id)

async def get_hash_table_use_case(
    unique_id: UniqueID = Depends(get_unique_id_instance),
    ) -> GetHashTableForStudentUseCase:
    return GetHashTableForStudentUseCaseImp(unique_id)

'''
def get_update_student_use_case(unit_of_work: StudentUnitOfWork = Depends(get_student_unit_of_work)) -> UpdateStudentUsecase:
    return UpdateStudentUsecaseImp(unit_of_work)
'''