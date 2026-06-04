import uuid
from datetime import datetime

from app.extensions import db


class DiscoveredQuery(db.Model):
    __tablename__ = "discovered_queries"

    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(36), unique=True, nullable=False, default=lambda: str(uuid.uuid4()))

    pipeline_run_id = db.Column(db.Integer, db.ForeignKey("pipeline_runs.id"), nullable=False)

    query_text = db.Column(db.Text, nullable=False)

    estimated_search_volume = db.Column(db.Integer, nullable=True)
    competitive_difficulty = db.Column(db.Integer, nullable=True)
    commercial_intent = db.Column(db.Float, nullable=True)

    domain_visible = db.Column(db.Boolean, default=False, nullable=False)
    visibility_position = db.Column(db.Integer, nullable=True)

    ai_response_excerpt = db.Column(db.Text, nullable=True)
    opportunity_score = db.Column(db.Float, nullable=True)

    created_at = db.Column(db.DateTime, default=datetime.now, nullable=False)

    pipeline_run = db.relationship("PipelineRun", back_populates="queries")
    recommendations = db.relationship(
        "ContentRecommendation",
        back_populates="discovered_query",
        cascade="all, delete-orphan",
    )