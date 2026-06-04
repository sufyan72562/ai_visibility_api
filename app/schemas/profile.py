from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class CreateProfileSchema(BaseModel):
    name: str = Field(..., min_length=1)
    domain: str = Field(..., min_length=1)
    industry: str = Field(..., min_length=1)

    description: Optional[str] = None
    competitors: list[str] = []


class ProfileResponseSchema(BaseModel):
    uuid: str

    name: str
    domain: str
    industry: str

    description: str | None
    competitors: list[str]

    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }