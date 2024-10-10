from .classroom import ClassroomModel
from app.core.models.convert_entity import ConvertEntity
from app.features.classroom.domain.entities.classroom_entity import ClassroomEntity
from app.features.classroom.domain.entities.classroom_schema import ClassroomDisplay, ClassroomUpdate
class ConvertClassroom(ConvertEntity):
    
    @staticmethod
    def to_entity(classroom_model: ClassroomModel) -> ClassroomEntity:
        return ClassroomEntity(
            id=classroom_model.id,
            number=classroom_model.number,
            created_at=classroom_model.created_at,
            updated_at=classroom_model.updated_at,
            is_deleted=classroom_model.is_deleted,
        )

    @staticmethod
    def to_dict(classroom_model: ClassroomModel) -> dict:
        return {
            'id': classroom_model.id,
            'number': classroom_model.number,
            'created_at': classroom_model.created_at,
            'updated_at': classroom_model.updated_at,
            'is_deleted': classroom_model.is_deleted,
        }
    
    @staticmethod
    def to_read_model(classroom_model: ClassroomModel) -> ClassroomDisplay:
        return ClassroomDisplay(
            id=classroom_model.id,
            number=classroom_model.number,
            created_at=classroom_model.created_at,
            updated_at=classroom_model.updated_at,
            is_deleted=classroom_model.is_deleted,
        )

    @staticmethod
    def from_entity(classroom_entity: ClassroomEntity) -> ClassroomModel:
        return ClassroomModel(
            id=classroom_entity.id,
            number=classroom_entity.number,
            created_at=classroom_entity.created_at,
            updated_at=classroom_entity.updated_at,
            is_deleted=classroom_entity.is_deleted
        )
    
        
    @staticmethod
    def updated_model(classroom_update: ClassroomUpdate, current_calssroom: ClassroomEntity) -> ClassroomEntity:
        model = ClassroomEntity(
            id=current_calssroom.id,
            name=classroom_update.name, 
            created_at=current_calssroom.created_at,  
            updated_at=current_calssroom.updated_at,
            is_deleted=current_calssroom.is_deleted  
        )
        
        return model