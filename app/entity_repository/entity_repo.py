from typing import Type, TypeVar, List, Optional
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from abc import abstractmethod

from app.core.models.mysql.models import BaseModel
from app.core.repositories.base_repository import BaseRepository
from app.core.util import hash

TEntity = TypeVar('TEntity')  
TModel = TypeVar('TModel', bound=BaseModel)

class EntityRepo(BaseRepository[TEntity]):
    def __init__(self, session: AsyncSession, model: Type[TModel]) -> None:
        self.session = session
        self.model = model

    @abstractmethod
    def to_entity(self, model_instance: TModel) -> TEntity:    # model to a domain entity
        pass

    @abstractmethod
    def from_entity(self, entity: TEntity) -> TModel:   # domain entity to a SQLAlchemy model

        pass

    @abstractmethod
    async def create_object(self, new_object: TEntity) -> TEntity:
        pass
    
    async def find_object_by_id(self, object_id: int) -> TEntity:
        result = await self.session.execute(select(self.model).filter(self.model.id == object_id))
        model_instance = result.scalars().first()
        return self.to_entity(model_instance) if model_instance else None

    async def find_all_objects(self) -> List[TEntity]:
        result = await self.session.execute(select(self.model))
        model_instances = result.scalars().all()
        return [self.to_entity(model_instance) for model_instance in model_instances]

    async def update_obj(self, update_obj: TEntity, current_obj: TEntity) -> TEntity:
        current_model = self.from_entity(current_obj)
        update_data = self.from_entity(update_obj)

        for var, value in vars(update_data).items():
            if value is not None:
                if var == 'password':
                    value = hash.get_password_hash(value)
                setattr(current_model, var, value) if value else None

        self.session.add(current_model)
        self.session.commit()
        return self.to_entity(current_model)

    async def delete_by_id(self, object_id: int) -> TEntity:
        model_instance = await self.find_object_by_id(object_id)
        if model_instance:
            return self.to_entity(model_instance)
        else:
            return None