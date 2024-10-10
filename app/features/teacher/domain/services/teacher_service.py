from abc import ABC, abstractmethod
from typing import Sequence
from app.core.services.entity_services import EntityServices
from app.features.teacher.domain.entities.teacher_schema import TeacherDisplay
from app.features.teacher.data.model import TeacherModel
from app.features.course.data.model import CourseModel


class TeacherService(EntityServices[TeacherDisplay, TeacherModel]):
    
    @abstractmethod
    async def find_courses_by_teacher_id(self, teacher_id: int) -> Sequence[CourseModel]:
        raise NotImplementedError()