from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from app.core.models.person import Person

class TeacherModel(Person):
    __tablename__ = 'teachers'
    
    courses = relationship('CourseModel', back_populates='teacher', cascade="all, delete-orphan")
