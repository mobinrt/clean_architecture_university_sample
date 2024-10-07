from app.core.unit_of_work.unit_of_work import AbstractUnitOfWork
from app.features.teacher.domain.repository.teacher_repo import TeacherRepository

from sqlalchemy.orm import Session
from abc import abstractmethod

class TeacherUnitOfWork(AbstractUnitOfWork[TeacherRepository]):
    def __init__(self, session: Session, teacher_repository: TeacherRepository):
        self.session: Session = session
        self.repository: TeacherRepository = teacher_repository

    @abstractmethod
    async def begin(self):
        raise NotImplementedError()
    
    @abstractmethod
    async def commit(self):
        raise NotImplementedError()
    
    @abstractmethod
    async def rollback(self):
        raise NotImplementedError()