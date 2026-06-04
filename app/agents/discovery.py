from app.agents.base import BaseAgent
from app.utils.enums import LLMResponseType


class QueryDiscoveryAgent(BaseAgent):
    def run(self, profile):
        prompt = self._build_prompt(profile)

        queries = self.llm_service.generate_json(prompt, 
                                                 LLMResponseType.QUERY_DISCOVERY)

        return queries

    def _build_prompt(self, profile):
        competitors = ", ".join(profile.competitors or [])

        return f"""
        You are a search intelligence expert.

        Business:
        Name: {profile.name}
        Domain: {profile.domain}
        Industry: {profile.industry}
        Description: {profile.description or "N/A"}
        Competitors: {competitors or "N/A"}

        Generate AI-search style queries that potential customers might ask
        when looking for products/services in this industry.

        Return JSON list with:
        - query
        - search_volume
        - difficulty
        - commercial_intent
        """