from abc import ABC

from app.core.services.entity_services import EntityServices
from app.features.teacher.domain.entities.teacher_schema import TeacherDisplay
from app.features.teacher.data.model import TeacherModel

class TeacherService(EntityServices[TeacherDisplay, TeacherModel]):
    pass