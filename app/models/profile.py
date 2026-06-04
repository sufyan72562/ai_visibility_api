import uuid
from datetime import datetime

from app.extensions import db


class BusinessProfile(db.Model):
    __tablename__ = "business_profiles"

    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(36), unique=True, nullable=False, default=lambda: str(uuid.uuid4()))

    name = db.Column(db.String(255), nullable=False)
    domain = db.Column(db.String(255), nullable=False)
    industry = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)

    competitors = db.Column(db.JSON, nullable=True)

    created_at = db.Column(db.DateTime, default=datetime.now, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)

    pipeline_runs = db.relationship(
        "PipelineRun",
        back_populates="profile",
        cascade="all, delete-orphan",
    )