from pydantic import BaseModel
from datetime import datetime

class ClassroomCreate(BaseModel):
    number: int
    
class ClassroomUpdate(BaseModel):
    number: int
    
class ClassroomDisplay(BaseModel):
    id: int
    number: int
    created_at: datetime | None = None
    updated_at: datetime | None = None
    is_deleted: bool | None = False
    
    model_config = {
        'from_attributes': True
    }
    