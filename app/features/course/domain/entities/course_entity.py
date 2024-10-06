import copy
from datetime import datetime
from typing import Any, Callable, TYPE_CHECKING
from datetime import date
from app.core.error.invalid_operation_exception import InvalidOperationError
from .course_schema import CourseUpdate
    
class CourseEntity(object):
    def __init__(
        self,
        id: int,
        name: int,
        start: date,
        end: date,
        teacher_id: int,
        class_id: int,
        created_at: datetime | None = None,
        updated_at: datetime | None = None,
        is_deleted: bool | None = False,
    ):
        self.id = id
        self.name = name
        self.start = start
        self.end = end
        self.teacher_id = teacher_id
        self.class_id = class_id 
        self.created_at = created_at
        self.updated_at = updated_at
        self.is_deleted = is_deleted

    def update_entity(self, entity_update_model: 'CourseUpdate', get_update_data: Callable[['CourseUpdate'], dict[str, Any]]
        ) -> 'CourseEntity':
        
        update_data = get_update_data(entity_update_model)
        update_entity = copy.deepcopy(self)

        for key, value in update_data.items():
            update_entity.__setattr__(key, value)

        return update_entity

    def mark_entity_as_deleted(self) -> 'CourseEntity':
        if self.is_deleted:
            raise InvalidOperationError('Course is already marked as deleted')

        marked_entity = copy.deepcopy(self)
        marked_entity.is_deleted = True

        return marked_entity

    def __eq__(self, other: object) -> bool:
        if isinstance(other, CourseEntity):
            return self.id == other.id

        return False

    def to_pop(self) -> object:
        return self.__dict__
