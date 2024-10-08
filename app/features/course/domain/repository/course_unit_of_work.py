from app.core.unit_of_work.unit_of_work import AbstractUnitOfWork
from app.features.course.domain.repository.course_repo import CourseRepository
from app.features.course.domain.services.course_service import CourseService

from sqlalchemy.orm import Session
from abc import abstractmethod

class CourseUnitOfWork(AbstractUnitOfWork[CourseRepository, CourseService]):
    def __init__(self, session: Session, course_repository: CourseRepository, course_service: CourseService):
        self.session: Session = session
        self.repository: CourseRepository = course_repository
        self.service: CourseService = course_service
        