from sqlalchemy.orm import Session

from app.features.classroom.domain.repository.classroom_repo import ClassroomRepository
from app.features.classroom.domain.repository.classroom_unite_of_work import ClassroomUnitOfWork
from app.features.classroom.domain.services.classroom_service import ClassroomService


class ClassroomUnitOfWorkImp(ClassroomUnitOfWork):
    
    def __init__(self, session: Session, classroom_repository: ClassroomRepository, classroom_service: ClassroomService):
        super().__init__(session, classroom_repository, classroom_service)
        
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