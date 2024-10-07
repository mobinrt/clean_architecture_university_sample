from sqlalchemy.orm import Session

from app.features.teacher.domain.repository.teache import StudentRepository
from app.features.student.domain.repository.student_unite_of_work import StudentUnitOfWork


class TeacherUnitOfWorkImp(StudentUnitOfWork):
    
    def __init__(self, session: Session, teacher_repository: StudentRepository):
        super().__init__(session, student_repository)
        
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