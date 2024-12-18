from sqlalchemy import Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.core.models.mysql.models import BaseModel
from app.features.teacher.data.model.teacher import TeacherModel
from app.features.classroom.data.model.classroom import ClassroomModel

class CourseModel(BaseModel):
    __tablename__ = 'courses'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    start: Mapped[Date] = mapped_column(Date)
    end: Mapped[Date] = mapped_column(Date)
    
    teacher_id = mapped_column(Integer, ForeignKey('teachers.id'))
    class_id = mapped_column(Integer, ForeignKey('classes.number'))

    students = relationship('StudentModel', secondary='student_course', back_populates='courses')
    
    teacher = relationship('TeacherModel', back_populates='courses')
    classes = relationship('ClassroomModel', back_populates='course')
