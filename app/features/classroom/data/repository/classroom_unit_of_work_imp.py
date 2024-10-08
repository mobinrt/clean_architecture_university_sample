from sqlalchemy.orm import Session

from app.features.classroom.domain.repository.classroom_repo import ClassroomRepository
from app.features.classroom.domain.repository.classroom_unite_of_work import ClassroomUnitOfWork


class ClassroomUnitOfWorkImp(ClassroomUnitOfWork):
    
    def __init__(self, session: Session, classroom_repository: ClassroomRepository):
        super().__init__(session, classroom_repository)
        
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