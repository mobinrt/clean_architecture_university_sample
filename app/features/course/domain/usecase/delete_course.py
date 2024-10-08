from abc import abstractmethod
from typing import Tuple

from app.core.util.id_manager import UniqueID
from app.core.use_cases.use_case import BaseUseCase
from app.core.error.course_exception import CourseNotFoundError, CourseIsDeletedError
from app.features.course.domain.entities.course_schema import CourseDisplay
from app.features.course.domain.repository.course_unit_of_work import CourseUnitOfWork

class DeleteCourseUseCase(BaseUseCase[Tuple[int], CourseDisplay]):
    uow: CourseUnitOfWork

    @abstractmethod
    def __call__(self, args: Tuple[int]) -> CourseDisplay:
        raise NotImplementedError()

class DeleteCourseUseCaseImpl(DeleteCourseUseCase):
    def __init__(self, uow: CourseUnitOfWork, unique_id: UniqueID):
        self.uow: CourseUnitOfWork = uow
        self.unique_id: UniqueID = unique_id

    async def __call__(self, args: Tuple[int]) -> CourseDisplay:
        id = args[0]
        existing_course_db = await self.uow.repository.find_object_by_id(id)
        
        if existing_course_db is None:
            raise CourseNotFoundError()
        
        existing_course_entity = self.uow.repository.to_entity(existing_course_db)
        
        try:
            if existing_course_db.is_deleted:
                raise CourseIsDeletedError()
                        
            marked_course_entity = existing_course_entity.mark_entity_as_deleted()
            marked_course_db = self.uow.repository.from_entity(marked_course_entity)
            await self.uow.session.merge(marked_course_db)
            await self.uow.commit()
        except Exception as e:
            await self.uow.rollback()
            raise e
        finally:
            pass
        
        return marked_course_db
