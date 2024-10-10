from app.features.auth.data.service.auth_service_imp import AuthServiceImp
from ...data.model import StudentModel

from sqlalchemy.ext.asyncio import AsyncSession


class StudentAuthService(AuthServiceImp[StudentModel]):
    def __init__(self, session: AsyncSession, model: StudentModel):
        self.session: AsyncSession = session
        self.model: StudentModel = model
        