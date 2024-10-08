from sqlalchemy import Integer
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.core.models.mysql.models import BaseModel

class ClassroomModel(BaseModel):
    __tablename__ = 'classes'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    number: Mapped[int] = mapped_column(Integer, index=True, unique=True)
    
    course = relationship('CourseModel', back_populates='classes', cascade="all, delete-orphan")
