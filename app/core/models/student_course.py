from sqlalchemy import Column, Table, Integer, ForeignKey

from app.core.db.database import db

student_course_association = Table(
    'student_course', db.Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('course_id', Integer, ForeignKey('courses.id'))
)
