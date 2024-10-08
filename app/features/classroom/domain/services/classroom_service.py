from abc import ABC

from app.core.services.entity_services import EntityServices
from app.features.classroom.domain.entities.classroom_schema import ClassroomDisplay
from app.features.classroom.data.model import ClassroomModel

class ClassroomService(EntityServices[ClassroomDisplay, ClassroomModel]):
    pass