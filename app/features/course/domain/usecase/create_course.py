from abc import abstractmethod
from typing import Tuple
from datetime import timedelta

from app.core.use_cases.use_case import BaseUseCase
from app.core.util.id_manager import UniqueID
from app.features.course.domain.entities.course_schema import CourseCreate
from app.features.course.domain.entities.course_entity import CourseEntity
from app.features.course.domain.entities.course_schema import CourseDisplay
from app.features.course.domain.repository.course_unit_of_work import CourseUnitOfWork
from app.core.enum.object_type_digit import ObjectDigits
from app.core.enum.object_type_str import ObjectToSTR
from app.core.error.course_exception import CourseNameValidError, CourseDateValidError, TeacherNotFoundError, ClassroomNotFoundError
from app.features.course.data.model.convert_course import ConvertCourse
from app.features.teacher.data.model import TeacherModel
from app.features.classroom.data.model import ClassroomModel

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
        
        if data.end - data.start < timedelta(days=10):
            raise CourseDateValidError()
        
        teacher = await self.uow.service.find_teacher_by_id(data.teacher_id)
        if not teacher:
            raise TeacherNotFoundError()
        
        classroom = await self.uow.service.find_classroom_by_number(data.class_id)
        if not classroom:
            raise ClassroomNotFoundError()
        
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
