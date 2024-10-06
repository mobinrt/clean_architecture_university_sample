from datetime import datetime
from sqlalchemy import Boolean, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy.sql import func
from app.core.db.database import db

class BaseModel(db.Base): 
    __abstract__ = True  

    created_at: Mapped[datetime] = mapped_column(TIMESTAMP, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        TIMESTAMP,
        server_default=func.now(),
        onupdate=func.current_timestamp()
    )
    is_deleted: Mapped[bool] = mapped_column(Boolean, default=False)
    
    