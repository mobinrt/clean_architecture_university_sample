from sqlalchemy.orm import Session

from app.features.course.domain.repository.course_repo import CourseRepository
from app.features.course.domain.repository.course_unit_of_work import CourseUnitOfWork
from app.features.course.domain.services.course_service import CourseService

class CourseUnitOfWorkImp(CourseUnitOfWork):
    
    def __init__(self, session: Session, course_repository: CourseRepository, course_service: CourseService):
        super().__init__(session, course_repository, course_service)
        
    async def begin(self):
        self.session = self.session

    async def commit(self):
        try:
            await self.session.commit()
        except Exception as e:
            await self.rollback()
            raise e

    async def rollback(self):
        await self.session.rollback()
        
    async def refresh(self, instance):
        await self.session.refresh(instance)    