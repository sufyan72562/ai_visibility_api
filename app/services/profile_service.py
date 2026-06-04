from app.extensions import db
from app.models.profile import BusinessProfile
from app.models.query import DiscoveredQuery
from app.models.pipeline_run import PipelineRun
from sqlalchemy import func


class ProfileService:

    @staticmethod
    def create(data):
        profile = BusinessProfile(**data)

        db.session.add(profile)
        db.session.commit()

        return profile

    @staticmethod
    def get_by_uuid(profile_uuid):
        return BusinessProfile.query.filter_by(
            uuid=profile_uuid
        ).first()

    @staticmethod
    def list():
        return BusinessProfile.query.all()
    
    @staticmethod
    def get_profile_summary(profile):
        result = (
            db.session.query(
                func.count(DiscoveredQuery.id),
                func.avg(DiscoveredQuery.opportunity_score),
            )
            .join(PipelineRun)
            .filter(
                PipelineRun.profile_id == profile.id
            )
            .first()
        )

        total_queries, avg_score = result

        return {
            "total_queries_discovered": total_queries or 0,
            "average_opportunity_score": round(
                avg_score or 0,
                2,
            ),
        }