from datetime import datetime
from pydantic import BaseModel


class RecommendationResponseSchema(BaseModel):
    uuid: str

    title: str
    content_type: str
    priority: str

    rationale: str
    target_keywords: list[str]

    created_at: datetime

    model_config = {
        "from_attributes": True
    }