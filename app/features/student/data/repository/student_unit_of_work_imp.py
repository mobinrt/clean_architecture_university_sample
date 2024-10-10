from sqlalchemy.orm import Session

from app.features.student.domain.repository.student_repo import StudentRepository
from app.features.student.domain.repository.student_unit_of_work import StudentUnitOfWork
from app.features.student.domain.services.student_service import StudentService

class StudentUnitOfWorkImp(StudentUnitOfWork):
    
    def __init__(self, session: Session, student_repository: StudentRepository, student_service: StudentService):
        super().__init__(session, student_repository, student_service)
        
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