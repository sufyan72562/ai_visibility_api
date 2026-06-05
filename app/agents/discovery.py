from app.agents.base import BaseAgent
from app.services.llm import LLMResponseType


class QueryDiscoveryAgent(BaseAgent):
    def run(self, profile):
        prompt = self._build_prompt(profile)

        result = self.llm_service.generate_json(
            prompt=prompt,
            response_type=LLMResponseType.QUERY_DISCOVERY,
        )

        return result["queries"]

    def _build_prompt(self, profile):
        competitors = ", ".join(profile.competitors or [])

        return f"""
                    Business profile:
                    - Name: {profile.name}
                    - Domain: {profile.domain}
                    - Industry: {profile.industry}
                    - Description: {profile.description or "N/A"}
                    - Competitors: {competitors or "N/A"}

                    Task:
                    Generate 10 to 20 AI-search style queries that potential customers may ask when researching this category.

                    Guidelines:
                    - Include comparison queries, alternative queries, problem-aware queries, and buying-intent queries.
                    - Queries should sound natural for AI assistants, not just Google keywords.
                    - Estimate search_volume, difficulty, and commercial_intent if exact data is unavailable.
                    - difficulty must be 0 to 100.
                    - commercial_intent must be 0 to 1.
                    """