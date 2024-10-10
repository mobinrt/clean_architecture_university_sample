from abc import abstractmethod

from app.shared.entity_repository.entity_repo import EntityRepo
from app.features.student.domain.entities.student_entity import StudentEntity
from app.features.student.data.model import StudentModel

class StudentRepository(EntityRepo[StudentEntity]):

    @abstractmethod
    async def enroll_student_in_course(self, course_id: int, student_id: int) -> StudentEntity | None:    
        raise NotImplementedError()

    '''
    @abstractmethod
    async def delete_mark(self, id: int) -> StudentEntity | None:
        raise NotImplementedError()
    '''