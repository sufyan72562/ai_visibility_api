from app.models.query import DiscoveredQuery
from app.models.pipeline_run import PipelineRun
from app.services.profile_service import ProfileService


class QueryService:
    @staticmethod
    def list_by_profile(profile_uuid: str):
        profile = ProfileService.get_by_uuid(profile_uuid)

        if not profile:
            raise ValueError("Profile not found")

        return (
            DiscoveredQuery.query
            .join(PipelineRun)
            .filter(PipelineRun.profile_id == profile.id)
            .order_by(DiscoveredQuery.created_at.desc())
            .all()
        )