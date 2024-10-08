from app.core.unit_of_work.unit_of_work import AbstractUnitOfWork
from app.features.teacher.domain.repository.teacher_repo import TeacherRepository
from app.features.teacher.domain.services.teacher_service import TeacherService

from sqlalchemy.orm import Session
from abc import abstractmethod

class TeacherUnitOfWork(AbstractUnitOfWork[TeacherRepository]):
    def __init__(self, session: Session, teacher_repository: TeacherRepository, teacher_service: TeacherService):
        self.session: Session = session
        self.repository: TeacherRepository = teacher_repository
        self.service: TeacherService = teacher_service