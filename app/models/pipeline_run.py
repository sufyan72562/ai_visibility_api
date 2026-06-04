import uuid
from datetime import datetime

from app.extensions import db


class PipelineRun(db.Model):
    __tablename__ = "pipeline_runs"

    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(36), unique=True, nullable=False, default=lambda: str(uuid.uuid4()))

    profile_id = db.Column(db.Integer, db.ForeignKey("business_profiles.id"), nullable=False)

    status = db.Column(db.String(50), nullable=False, default="pending")
    error_message = db.Column(db.Text, nullable=True)

    queries_discovered = db.Column(db.Integer, default=0)
    queries_scored = db.Column(db.Integer, default=0)
    recommendations_generated = db.Column(db.Integer, default=0)

    started_at = db.Column(db.DateTime, default=datetime.now, nullable=False)
    completed_at = db.Column(db.DateTime, nullable=True)

    profile = db.relationship("BusinessProfile", back_populates="pipeline_runs")
    queries = db.relationship(
        "DiscoveredQuery",
        back_populates="pipeline_run",
        cascade="all, delete-orphan",
    )