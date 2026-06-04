from app.models.query import DiscoveredQuery
from app.models.pipeline_run import PipelineRun
from app.services.profile_service import ProfileService


class QueryService:
    VALID_STATUSES = {"visible", "not_visible", "unknown"}

    @staticmethod
    def list_by_profile(
        profile_uuid: str,
        min_score: float | None = None,
        status: str | None = None,
        page: int = 1,
        per_page: int = 20,
    ):
        profile = ProfileService.get_by_uuid(profile_uuid)

        if not profile:
            raise ValueError("Profile not found")

        if status and status not in QueryService.VALID_STATUSES:
            raise ValueError("Invalid status filter")

        page = max(page, 1)
        per_page = min(max(per_page, 1), 100)

        query = (
            DiscoveredQuery.query
            .join(DiscoveredQuery.pipeline_run)
            .filter(PipelineRun.profile_id == profile.id)
        )

        if min_score is not None:
            query = query.filter(DiscoveredQuery.opportunity_score >= min_score)

        if status == "visible":
            query = query.filter(DiscoveredQuery.domain_visible.is_(True))

        elif status == "not_visible":
            query = query.filter(DiscoveredQuery.domain_visible.is_(False))

        elif status == "unknown":
            query = query.filter(DiscoveredQuery.opportunity_score.is_(None))

        return (
            query
            .order_by(DiscoveredQuery.opportunity_score.desc().nullslast())
            .paginate(
                page=page,
                per_page=per_page,
                error_out=False,
            )
        )