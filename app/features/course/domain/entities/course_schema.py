from datetime import datetime, date
from pydantic import BaseModel

class CourseCreate(BaseModel):
    name: str
    start: date
    end: date
    teacher_id: int
    class_id: int

class CourseUpdate(BaseModel):
    name: str
    start: date
    end: date
    
class CourseDisplay(BaseModel):
    id: int
    name: str
    start: date
    end: date
    teacher_id: int
    class_id: int
    created_at: datetime | None = None
    updated_at: datetime | None = None
    is_deleted: bool | None = False
    
    model_config = {
        'from_attributes': True
    }
    