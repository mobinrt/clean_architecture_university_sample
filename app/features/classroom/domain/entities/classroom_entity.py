import copy
from datetime import datetime
from typing import Any, Callable, TYPE_CHECKING

from app.core.error.invalid_operation_exception import InvalidOperationError
from app.features.classroom.domain.entities.classroom_schema import ClassroomUpdate
    
class ClassroomEntity(object):
    def __init__(
        self,
        id: int,
        number: int,
        created_at: datetime | None = None,
        updated_at: datetime | None = None,
        is_deleted: bool | None = False,
    ):
        self.id = id
        self.number = number
        self.created_at = created_at
        self.updated_at = updated_at
        self.is_deleted = is_deleted

    def update_entity(self, entity_update_model: 'ClassroomUpdate', get_update_data: Callable[['ClassroomUpdate'], dict[str, Any]]
        ) -> 'ClassroomEntity':
        
        update_data = get_update_data(entity_update_model)
        update_entity = copy.deepcopy(self)

        for key, value in update_data.items():
            update_entity.__setattr__(key, value)

        return update_entity

    def mark_entity_as_deleted(self) -> 'ClassroomEntity':
        if self.is_deleted:
            raise InvalidOperationError('Classroom is already marked as deleted')

        marked_entity = copy.deepcopy(self)
        marked_entity.is_deleted = True

        return marked_entity

    def __eq__(self, other: object) -> bool:
        if isinstance(other, ClassroomEntity):
            return self.id == other.id

        return False

    def to_pop(self) -> object:
        return self.__dict__
