from abc import ABC, abstractmethod
from typing import TypeVar, Generic

_T = TypeVar('_T')


class AbstractUnitOfWork(ABC, Generic[_T]):

    repository: _T

    @abstractmethod
    async def begin(self):
        raise NotImplementedError()

    @abstractmethod
    async def commit(self):
        raise NotImplementedError()

    @abstractmethod
    async def rollback(self):
        raise NotImplementedError()