from app.core.unit_of_work.unit_of_work import AbstractUnitOfWork
from app.features.student.domain.repository.student_repo import StudentRepository
from app.features.student.domain.services.student_service import StudentService

from sqlalchemy.orm import Session

class StudentUnitOfWork(AbstractUnitOfWork[StudentRepository, StudentService]):
    def __init__(self, session: Session, student_repository: StudentRepository, student_service: StudentService):
        self.session: Session = session
        self.repository: StudentRepository = student_repository
        self.service: StudentService = student_service

    