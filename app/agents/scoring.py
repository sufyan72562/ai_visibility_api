from app.agents.base import BaseAgent
from app.services.llm import LLMResponseType
from app.utils.scoring import calculate_opportunity_score


class VisibilityScoringAgent(BaseAgent):
    def run(self, profile, discovered_query):
        prompt = self._build_prompt(profile, discovered_query)

        result = self.llm_service.generate_json(
            prompt=prompt,
            response_type=LLMResponseType.VISIBILITY_SCORING,
        )

        domain_visible = result["domain_visible"]

        opportunity_score = calculate_opportunity_score(
            search_volume=discovered_query.estimated_search_volume,
            difficulty=discovered_query.competitive_difficulty,
            commercial_intent=discovered_query.commercial_intent,
            domain_visible=domain_visible,
        )

        return {
            "domain_visible": domain_visible,
            "visibility_position": result["visibility_position"],
            "ai_response_excerpt": result["ai_response_excerpt"],
            "opportunity_score": opportunity_score,
        }

    def _build_prompt(self, profile, discovered_query):
        competitors = ", ".join(profile.competitors or [])

        return f"""
                    Business to evaluate:
                    - Name: {profile.name}
                    - Domain: {profile.domain}
                    - Industry: {profile.industry}
                    - Competitors: {competitors or "N/A"}

                    Query:
                    {discovered_query.query_text}

                    Task:
                    Estimate whether this business would appear in a high-quality AI-generated answer for this query.

                    Rules:
                    - domain_visible is true if the brand name or domain is likely to be mentioned.
                    - visibility_position is the likely mention position among recommended brands/tools.
                    - Use null for visibility_position if the business is not visible.
                    - ai_response_excerpt should briefly explain what the AI answer would likely mention.
                    - Be conservative if uncertain.
                    """