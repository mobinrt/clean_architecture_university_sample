from .course import CourseModel
from app.core.models.convert_entity import ConvertEntity
from app.features.course.domain.entities.course_entity import CourseEntity
from app.features.course.domain.entities.course_schema import CourseDisplay
class ConvertCourse(ConvertEntity):
    
    @staticmethod
    def to_entity(course_model: CourseModel) -> CourseEntity:
        return CourseEntity(
            id=course_model.id,
            name=course_model.name,
            start=course_model.start,
            end=course_model.end,
            teacher_id=course_model.teacher_id,
            class_id=course_model.class_id,
            created_at=course_model.created_at,
            updated_at=course_model.updated_at,
            is_deleted=course_model.is_deleted,
        )

    @staticmethod
    def to_dict(course_model: CourseModel) -> dict:
        return {
            'id': course_model.id,
            'name': course_model.name,
            'start': course_model.start,
            'end': course_model.end,
            'teacher_id': course_model.teacher_id,
            'class_id': course_model.class_id,
            'created_at': course_model.created_at,
            'updated_at': course_model.updated_at,
            'is_deleted': course_model.is_deleted,
        }
    
    @staticmethod
    def to_read_model(course_model: CourseModel) -> CourseDisplay:
        return CourseDisplay(
            id=course_model.id,
            name=course_model.name,
            start=course_model.start,
            end=course_model.end,
            teacher_id=course_model.teacher_id,
            class_id=course_model.class_id,
            created_at=course_model.created_at,
            updated_at=course_model.updated_at,
            is_deleted=course_model.is_deleted,
        )

    @staticmethod
    def from_entity(course_entity: CourseEntity) -> CourseModel:
        return CourseModel(
            id=course_entity.id,
            name=course_entity.name,
            start=course_entity.start,
            end=course_entity.end,
            teacher_id=course_entity.teacher_id,
            class_id=course_entity.class_id,
            created_at=course_entity.created_at,
            updated_at=course_entity.updated_at,
            is_deleted=course_entity.is_deleted
        )
