from app.core.unit_of_work.unit_of_work import AbstractUnitOfWork
from app.features.student.domain.repository.student_repo import StudentRepository

from sqlalchemy.orm import Session
from abc import abstractmethod

class StudentUnitOfWork(AbstractUnitOfWork[StudentRepository]):
    def __init__(self, session: Session, student_repository: StudentRepository):
        self.session: Session = session
        self.repository: StudentRepository = student_repository
    
    