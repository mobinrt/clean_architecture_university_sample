from abc import abstractmethod

from app.entity_repository.entity_repo import EntityRepo
from app.features.teacher.domain.entities.teacher_entity import TeacherEntity
from app.features.teacher.data.model import TeacherModel
class TeacherRepository(EntityRepo[TeacherEntity]):
    pass