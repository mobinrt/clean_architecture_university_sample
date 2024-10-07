import copy
from datetime import datetime
from typing import Any, Callable, TYPE_CHECKING

from app.features.student.data.model import StudentModel
from app.core.error.student_exception import StudentIsDeleted
from app.core.enum.major import Major
from app.features.student.domain.entities.student_schema import StudentUpdate
from app.core.util import hash
class StudentEntity(object):        #TODO: set father for entities
    def __init__(
        self,
        id: int,
        name: str,
        password: str,
        major: Major,
        created_at: datetime | None = None,
        updated_at: datetime | None = None,
        is_deleted: bool | None = False,
    ):
        self.id = id
        self.name = name
        self.password = password
        self.major = major
        self.created_at = created_at
        self.updated_at = updated_at
        self.is_deleted = is_deleted

    def update_entity(self, entity_update_model: StudentUpdate, get_update_data: Callable[[StudentUpdate], dict[str, Any]]
        ) -> 'StudentEntity':
        
        update_data = get_update_data(entity_update_model)
        update_entity = copy.deepcopy(self)

        for key, value in update_data.items():
            if key == 'password':
                value = hash.get_password_hash(value)  
            update_entity.__setattr__(key, value)

        return update_entity

    def mark_entity_as_deleted(self) -> 'StudentEntity':
        if self.is_deleted:
            raise StudentIsDeleted()
        
        marked_entity = copy.deepcopy(self)
        marked_entity.is_deleted = True
        
        return marked_entity

    def __eq__(self, other: object) -> bool:
        if isinstance(other, StudentEntity):
            return self.id == other.id

        return False

    def to_pop(self) -> object:
        return self.__dict__
