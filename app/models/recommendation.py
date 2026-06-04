import uuid
from datetime import datetime

from app.extensions import db


class ContentRecommendation(db.Model):
    __tablename__ = "content_recommendations"

    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(36), unique=True, nullable=False, default=lambda: str(uuid.uuid4()))

    query_id = db.Column(db.Integer, db.ForeignKey("discovered_queries.id"), nullable=False)

    title = db.Column(db.String(255), nullable=False)
    content_type = db.Column(db.String(100), nullable=False)
    priority = db.Column(db.String(50), nullable=False)

    rationale = db.Column(db.Text, nullable=True)
    target_keywords = db.Column(db.JSON, nullable=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    query = db.relationship("DiscoveredQuery", back_populates="recommendations")