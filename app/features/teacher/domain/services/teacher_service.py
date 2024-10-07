from abc import ABC

from app.core.services.entity_services import EntityServices
from app.features.student.domain.entities.student_schema import StudentDisplay
from app.features.student.data.model import StudentModel
from ..entities import StudentDisplay

class StudentService(EntityServices[StudentDisplay, StudentModel]):
    pass