from pydantic import BaseModel, Field


class PersonBaseModel(BaseModel):
    name: str = Field(..., pattern=r"^[a-z]+$")
    