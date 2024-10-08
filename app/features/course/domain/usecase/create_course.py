from abc import abstractmethod
from typing import Tuple

from app.core.use_cases.use_case import BaseUseCase
from app.core.util.id_manager import UniqueID
from app.features.course.domain.entities.course_schema import CourseCreate
from app.features.course.domain.entities.course_entity import CourseEntity
from app.features.course.domain.entities.course_schema import CourseDisplay
from app.features.course.domain.repository.course_unit_of_work import CourseUnitOfWork
from app.core.enum.object_type_digit import ObjectDigits
from app.core.enum.object_type_str import ObjectToSTR
from app.core.error.course_exception import CourseNameValidError, CourseDateValidError
from app.features.course.data.model.convert_course import ConvertCourse
from datetime import timedelta

class CreateCourseUseCase(BaseUseCase[Tuple[CourseCreate], CourseDisplay]):
    uow: CourseUnitOfWork

    @abstractmethod
    async def __call__(self, args: Tuple[CourseCreate]) -> CourseDisplay:
        raise NotImplementedError()

class CreateCourseUseCaseImp(CreateCourseUseCase):
    def __init__(self, uow: CourseUnitOfWork, unique_id: UniqueID):
        self.uow: CourseUnitOfWork = uow
        self.unique_id: UniqueID = unique_id
        
    async def __call__(self, args: Tuple[CourseCreate]) -> CourseDisplay:
        data = args[0]
        
        if not data.name:
            raise CourseNameValidError()
        
        if new_course.end - new_course.start < timedelta(days=10):
            raise CourseDateValidError()
        
        teacher = await self.uow.repository.get_object_by_id_filter_model(new_course.teacher_id, TeacherModel)
        if not teacher:
            raise 
        
        classroom = await self.service.get_object_by_id_filter_model(new_course.class_id, ClassModel)
        if not classroom:
            raise 
        course_id = self.unique_id.insert(ObjectDigits.COURSE.value, ObjectToSTR.COURSE.value)

        new_course = CourseEntity(
            id=course_id,
            **data.model_dump()
        )
        try:
            await self.uow.repository.create_object(new_course, course_id)
            self.unique_id.save_to_dict(new_course.name, new_course.id, ObjectToSTR.COURSE.value)
            await self.uow.commit()
            return ConvertCourse.from_entity(new_course)
        except Exception as e:
            await self.uow.rollback()
            raise e
