from .teacher import TeacherModel
from app.core.models.convert_entity import ConvertEntity
from app.features.teacher.domain.entities.teacher_entity import TeacherEntity
from app.features.teacher.domain.entities.teacher_schema import TeacherDisplay, TeacherUpdate
class ConvertTeacher(ConvertEntity):
    
    @staticmethod
    def to_entity(teacher_model: TeacherModel) -> TeacherEntity:
        return TeacherEntity(
            id=teacher_model.id,
            name=teacher_model.name,
            password=teacher_model.password,
            created_at=teacher_model.created_at,
            updated_at=teacher_model.updated_at,
            is_deleted=teacher_model.is_deleted,
        )

    @staticmethod
    def to_dict(teacher_model: TeacherModel) -> dict:
        return {
            'id': teacher_model.id,
            'name': teacher_model.name,
            'password': teacher_model.password,
            'created_at': teacher_model.created_at,
            'updated_at': teacher_model.updated_at,
            'is_deleted': teacher_model.is_deleted,
        }
    
    @staticmethod
    def to_read_model(teacher_model: TeacherModel) -> TeacherDisplay:
        return TeacherDisplay(
            id=teacher_model.id,
            name=teacher_model.name,
            is_deleted=teacher_model.is_deleted,
            created_at=teacher_model.created_at,
            updated_at=teacher_model.updated_at,
        )

    @staticmethod
    def from_entity(teacher_entity: TeacherEntity) -> TeacherModel:
        return TeacherModel(
            id=teacher_entity.id,
            name=teacher_entity.name,
            password=teacher_entity.password,
            created_at=teacher_entity.created_at,
            updated_at=teacher_entity.updated_at,
            is_deleted=teacher_entity.is_deleted
        )

    @staticmethod
    def updated_model(teacher_update: TeacherUpdate, current_user: TeacherEntity) -> TeacherEntity:
        model = TeacherEntity(
            id=current_user.id,
            name=teacher_update.name, 
            password=teacher_update.password,
            created_at=current_user.created_at,  
            updated_at=current_user.updated_at,
            is_deleted=current_user.is_deleted  
        )
        return model