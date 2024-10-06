from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from .mysql.models import BaseModel

class Person(BaseModel):
    __abstract__ = True
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(50), index=True)
    password: Mapped[str] = mapped_column(String(250), nullable=False)
    
    