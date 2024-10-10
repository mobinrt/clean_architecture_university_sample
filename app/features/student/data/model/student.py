from sqlalchemy import Enum
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped, mapped_column
from app.features.course.data.model.course import CourseModel 
from .....core.models.student_course import student_course_association
from app.core.models.person import Person
from app.core.enum.major import Major
class StudentModel(Person):
    
    __tablename__ = 'students'
    
    major: Mapped[Major] = mapped_column(Enum(Major), nullable=False)
    courses = relationship('CourseModel', secondary=student_course_association, back_populates='students')
 