from pydantic import Field

from app.core.schema.schema_person import PersonCreate, PersonUpdate, PersonDisplay
from app.core.enum.major import Major

class StudentCreate(PersonCreate):
    major: Major = Field(..., description='Select your field: ' 
                            '1) computer_science '
                            '2) electrical_engineering '
                            '3) mathematics' 
                            '4) physics')

class StudentUpdate(PersonUpdate):
    pass


class StudentDisplay(PersonDisplay):
    major: Major
    
    class Config:
        use_enum_values = True

    