from abc import abstractmethod

from app.entity_repository.entity_repo import EntityRepo
from app.features.classroom.domain.entities.classroom_entity import ClassroomEntity
from app.features.classroom.data.model import ClassroomModel
from abc import abstractmethod

class ClassroomRepository(EntityRepo[ClassroomEntity]):

    @abstractmethod
    async def find_classroom_by_number(self, class_num: int):
        raise NotImplementedError()