from abc import ABC, abstractmethod
from typing import TypeVar, Generic

_R = TypeVar('_R')
_S = TypeVar('_S')

class AbstractUnitOfWork(ABC, Generic[_R, _S]):

    repository: _R
    service: _S
    
    @abstractmethod
    async def begin(self):
        raise NotImplementedError()

    @abstractmethod
    async def commit(self):
        raise NotImplementedError()

    @abstractmethod
    async def rollback(self):
        raise NotImplementedError()
    
    @abstractmethod
    async def refresh(self, instance):
        raise NotImplementedError()