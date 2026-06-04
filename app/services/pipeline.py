from datetime import datetime

from app.extensions import db
from app.models.pipeline_run import PipelineRun
from app.services.profile_service import ProfileService


class PipelineService:
    @staticmethod
    def run(profile_uuid: str) -> PipelineRun:
        profile = ProfileService.get_by_uuid(profile_uuid)

        if not profile:
            raise ValueError("Profile not found")

        pipeline_run = PipelineRun(
            profile_id=profile.id,
            status="running",
        )

        db.session.add(pipeline_run)
        db.session.commit()

        try:
            # Temporary placeholders
            # Later yahan agents call honge:
            # 1. QueryDiscoveryAgent
            # 2. VisibilityScoringAgent
            # 3. ContentRecommendationAgent

            pipeline_run.queries_discovered = 0
            pipeline_run.queries_scored = 0
            pipeline_run.recommendations_generated = 0

            pipeline_run.status = "completed"
            pipeline_run.completed_at = datetime.utcnow()

            db.session.commit()

        except Exception as exc:
            pipeline_run.status = "failed"
            pipeline_run.error_message = str(exc)
            pipeline_run.completed_at = datetime.utcnow()

            db.session.commit()

        return pipeline_run