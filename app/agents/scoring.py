from app.agents.base import BaseAgent
from app.utils.scoring import calculate_opportunity_score


class VisibilityScoringAgent(BaseAgent):
    def run(self, profile, discovered_query):
        prompt = self._build_prompt(profile, discovered_query)

        result = self.llm_service.generate_visibility_json(prompt)

        domain_visible = result.get("domain_visible", False)

        opportunity_score = calculate_opportunity_score(
            search_volume=discovered_query.estimated_search_volume,
            difficulty=discovered_query.competitive_difficulty,
            commercial_intent=discovered_query.commercial_intent,
            domain_visible=domain_visible,
        )

        return {
            "domain_visible": domain_visible,
            "visibility_position": result.get("visibility_position"),
            "ai_response_excerpt": result.get("ai_response_excerpt"),
            "opportunity_score": opportunity_score,
        }

    def _build_prompt(self, profile, discovered_query):
        return f"""
        You are an AI search visibility evaluator.

        Business:
        Name: {profile.name}
        Domain: {profile.domain}
        Industry: {profile.industry}

        Query:
        {discovered_query.query_text}

        Check whether this business would appear in an AI-generated answer
        for this query.

        Return JSON with:
        - domain_visible: boolean
        - visibility_position: number or null
        - ai_response_excerpt: short text
        """