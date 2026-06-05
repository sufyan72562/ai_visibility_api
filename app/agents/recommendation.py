from app.agents.base import BaseAgent
from app.services.llm import LLMResponseType


class ContentRecommendationAgent(BaseAgent):
    def run(self, profile, query):
        prompt = self._build_prompt(profile, query)

        return self.llm_service.generate_json(
            prompt=prompt,
            response_type=LLMResponseType.CONTENT_RECOMMENDATION,
        )

    def _build_prompt(self, profile, query):
        return f"""
                    Business:
                    - Name: {profile.name}
                    - Domain: {profile.domain}
                    - Industry: {profile.industry}
                    - Description: {profile.description or "N/A"}

                    Query opportunity:
                    - Query: {query.query_text}
                    - Search volume: {query.estimated_search_volume}
                    - Difficulty: {query.competitive_difficulty}
                    - Commercial intent: {query.commercial_intent}
                    - Domain visible: {query.domain_visible}
                    - Visibility position: {query.visibility_position}
                    - Opportunity score: {query.opportunity_score}

                    Task:
                    Recommend one content asset to improve visibility for this query.

                    Guidelines:
                    - Make the title specific and publishable.
                    - Choose the most suitable content_type.
                    - Priority should reflect opportunity score and visibility gap.
                    - Rationale should explain why this content helps.
                    - Include 3 to 8 target keywords.
                    """