from abc import ABC, abstractmethod
from typing import Sequence, TypeVar, Generic

from app.core.models.mysql.models import BaseModel

_Display = TypeVar('_Display')
_Model = TypeVar('_Model', bound=BaseModel)

class EntityServices(ABC, Generic[_Display, _Model]):
    
    @abstractmethod
    def to_read_model(model: _Model) -> _Display:
        pass

    @abstractmethod
    def find_object_by_id(self, id: int) -> _Display | None:
        raise NotImplementedError()

    @abstractmethod
    def find_all_objects(self) -> Sequence[_Display]:
        raise NotImplementedError()
