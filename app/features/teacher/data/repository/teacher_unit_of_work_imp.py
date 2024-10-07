from sqlalchemy.orm import Session

from app.features.teacher.domain.repository.teacher_repo import TeacherRepository
from app.features.teacher.domain.repository.teacher_unite_of_work import TeacherUnitOfWork


class TeacherUnitOfWorkImp(TeacherUnitOfWork):
    
    def __init__(self, session: Session, teacher_repository: TeacherRepository):
        super().__init__(session, teacher_repository)
        
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