from abc import ABC, abstractmethod
from typing import TypeVar, Sequence, Generic

_T = TypeVar('_T')


class BaseRepository(ABC, Generic[_T]):
    @abstractmethod
    async def create_object(self, entity: _T):
        raise NotImplementedError()

    @abstractmethod
    async def find_all_objects(self) -> Sequence[_T]:
        raise NotImplementedError()

    @abstractmethod
    async def find_object_by_id(self, id_: int) -> _T | None:
        raise NotImplementedError()

    @abstractmethod
    async def update_obj(self, entity: _T) -> _T:
        raise NotImplementedError()

    @abstractmethod
    async def delete_by_id(self, id_: int) -> None:
        raise NotImplementedError()
