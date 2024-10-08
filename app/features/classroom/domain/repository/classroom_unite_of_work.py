from app.core.unit_of_work.unit_of_work import AbstractUnitOfWork
from app.features.classroom.domain.repository.classroom_repo import ClassroomRepository

from sqlalchemy.orm import Session
from abc import abstractmethod

class ClassroomUnitOfWork(AbstractUnitOfWork[ClassroomRepository]):
    def __init__(self, session: Session, classroom_repository: ClassroomRepository):
        self.session: Session = session
        self.repository: ClassroomRepository = classroom_repository

    