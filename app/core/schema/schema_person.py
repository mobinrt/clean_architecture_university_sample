from pydantic import BaseModel, Field, model_validator
from typing import Optional
from datetime import datetime

from .schema_base_person import PersonBaseModel
from ..db.database import db

class PersonCreate(PersonBaseModel):
    password: str = Field(min_length=6, max_length=16)
    confirm_password: str

    @model_validator(mode='before')
    def check_passwords_match(cls, values):
        password = values.get('password')
        confirm_password = values.get('confirm_password')
        if password != confirm_password:
            raise ValueError('Passwords do not match!!')
        return values

class PersonDisplay(PersonBaseModel):
    id: int
    created_at: datetime 
    updated_at: datetime
    is_deleted: bool | None = False
        
    model_config = {
        'from_attributes': True
    }
    
class PersonUpdate(PersonBaseModel):
    password: Optional[str] = Field(None, min_length=6, max_length=16)
    confirm_password: str

    @model_validator(mode='before')
    def check_passwords_match(cls, values):
        password = values.get('password')
        confirm_password = values.get('confirm_password')
        if password != confirm_password:
            raise ValueError('Passwords do not match!!')
        return values

