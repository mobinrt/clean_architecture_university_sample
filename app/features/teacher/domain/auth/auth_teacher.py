from app.features.auth.data.service.auth_service_imp import AuthServiceImp
from ...data.model import TeacherModel

from sqlalchemy.ext.asyncio import AsyncSession


class StudentAuthService(AuthServiceImp[TeacherModel]):
    def __init__(self, session: AsyncSession, model: TeacherModel):
        self.session: AsyncSession = session
        self.model: TeacherModel = model
        