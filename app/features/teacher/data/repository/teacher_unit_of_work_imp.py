from sqlalchemy.orm import Session

from app.features.teacher.domain.repository.teacher_repo import TeacherRepository
from app.features.teacher.domain.repository.teacher_unite_of_work import TeacherUnitOfWork
from app.features.teacher.domain.services.teacher_service import TeacherService

class TeacherUnitOfWorkImp(TeacherUnitOfWork):
    
    def __init__(self, session: Session, teacher_repository: TeacherRepository, teacher_service: TeacherService):
        super().__init__(session, teacher_repository, teacher_service)
        
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