from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class PipelineRunResponseSchema(BaseModel):
    uuid: str
    status: str
    queries_discovered: int
    queries_scored: int
    recommendations_generated: int
    error_message: Optional[str]
    started_at: datetime
    completed_at: Optional[datetime]

    model_config = {
        "from_attributes": True
    }