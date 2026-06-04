from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class QueryResponseSchema(BaseModel):
    uuid: str
    query_text: str
    estimated_search_volume: Optional[int]
    competitive_difficulty: Optional[int]
    commercial_intent: Optional[float]
    domain_visible: bool
    visibility_position: Optional[int]
    ai_response_excerpt: Optional[str]
    opportunity_score: Optional[float]
    created_at: datetime

    model_config = {
        "from_attributes": True
    }