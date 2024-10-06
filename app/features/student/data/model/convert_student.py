from . import StudentModel
from app.core.models.convert_entity import ConvertEntity
from app.features.student.domain.entities.student_entity import StudentEntity
from app.features.student.domain.entities.student_schema import StudentDisplay

class ConvertStudent(ConvertEntity):
    
    @staticmethod
    def to_entity(student_model: StudentModel) -> StudentEntity:
        return StudentEntity(
            id=student_model.id,
            name=student_model.name,
            major=student_model.major,
            password=student_model.password,
            created_at=student_model.created_at,
            updated_at=student_model.updated_at,
            is_deleted=student_model.is_deleted,
        )

    @staticmethod
    def to_dict(student_model: StudentModel) -> dict:
        return {
            'id': student_model.id,
            'name': student_model.name,
            'major': student_model.major,
            'password': student_model.password,
            'created_at': student_model.created_at,
            'updated_at': student_model.updated_at,
            'is_deleted': student_model.is_deleted,
        }
    
    @staticmethod
    def to_read_model(student_model: StudentModel) -> StudentDisplay:
        return StudentDisplay(
            id=student_model.id,
            name=student_model.name,
            major=student_model.major,
            is_deleted=student_model.is_deleted,
            created_at=student_model.created_at,
            updated_at=student_model.updated_at,
        )
        
    @staticmethod
    def from_entity(student_entity: StudentEntity) -> StudentModel:
        return StudentModel(
            id=student_entity.id,
            name=student_entity.name,
            major=student_entity.major,
            password=student_entity.password,
            created_at=student_entity.created_at,
            updated_at=student_entity.updated_at,
            is_deleted=student_entity.is_deleted
        )
