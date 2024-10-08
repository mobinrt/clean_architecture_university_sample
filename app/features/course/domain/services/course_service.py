from abc import ABC

from app.core.services.entity_services import EntityServices
from app.features.course.data.model import CourseModel
from ..entities.course_schema import CourseDisplay

class CourseService(EntityServices[CourseDisplay, CourseModel]):
    pass