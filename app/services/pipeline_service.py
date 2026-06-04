from datetime import datetime

from app.extensions import db
from app.models.pipeline_run import PipelineRun
from app.models.query import DiscoveredQuery
from app.services.profile_service import ProfileService
from app.services.llm import LLMService
from app.agents.discovery import QueryDiscoveryAgent


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
            llm_service = LLMService()

            discovery_agent = QueryDiscoveryAgent(llm_service)
            discovered_queries = discovery_agent.run(profile)

            for item in discovered_queries:
                query = DiscoveredQuery(
                    pipeline_run_id=pipeline_run.id,
                    query_text=item["query"],
                    estimated_search_volume=item.get("search_volume"),
                    competitive_difficulty=item.get("difficulty"),
                    commercial_intent=item.get("commercial_intent"),
                )

                db.session.add(query)

            pipeline_run.queries_discovered = len(discovered_queries)
            pipeline_run.queries_scored = 0
            pipeline_run.recommendations_generated = 0
            pipeline_run.status = "completed"
            pipeline_run.completed_at = datetime.now()

            db.session.commit()

        except Exception as exc:
            pipeline_run.status = "failed"
            pipeline_run.error_message = str(exc)
            pipeline_run.completed_at = datetime.now()

            db.session.commit()

        return pipeline_run