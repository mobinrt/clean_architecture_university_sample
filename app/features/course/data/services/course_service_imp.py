from sqlalchemy.future import select
from sqlalchemy.orm import Session
from typing import Sequence
from typing import Type, TypeVar

from ..model import CourseModel
from app.features.course.domain.services.course_service import CourseService
from app.features.course.domain.entities.course_schema import CourseDisplay
from app.features.course.data.model.convert_course import ConvertCourse
from app.features.classroom.data.model import ClassroomModel
from app.features.teacher.data.model import TeacherModel

_MODEL = TypeVar('_MODEL')  

class CourseServiceImp(CourseService):
    
    def __init__(self, session: Session):
        self.session: Session = session

    def to_read_model(self, course_model: CourseModel) -> CourseDisplay:
        return ConvertCourse.to_read_model(course_model)

    async def find_object_by_id(self, id: int) -> CourseDisplay | None:
        result = await self.session.execute(select(CourseModel).filter(CourseModel.id == id))
        model_instance = result.scalars().first()
        print(model_instance)
        return self.to_read_model(model_instance) if model_instance else None

    async def find_all_objects(self) -> Sequence[CourseDisplay]:
        result = await self.session.execute(select(CourseModel))
        model_instances = result.scalars().all()
        return [self.to_read_model(model_instance) for model_instance in model_instances]
    
    async def find_teacher_by_id(self, teahcer_id: int):
        result = await self.session.execute(select(TeacherModel).filter(TeacherModel.id == teahcer_id))
        model_instance = result.scalars().first()
        return model_instance
    
    async def find_classroom_by_number(self, classroom_num: int):
        result = await self.session.execute(select(ClassroomModel).filter(ClassroomModel.number == classroom_num))
        model_instance = result.scalars().first()
        return model_instance

    async def find_object_by_id_filter_model(self, object_id: int, model: Type[_MODEL]) -> _MODEL | None:
        result = await self.session.execute(select(model).filter(model.id == object_id))
        model_instance = result.scalars().first()
        return model_instance
