from app.agents.base import BaseAgent
from app.utils.enums import LLMResponseType


class ContentRecommendationAgent(BaseAgent):
    def run(self, profile, query):
        prompt = self._build_prompt(profile, query)
        return self.llm_service.generate_json(prompt, LLMResponseType.CONTENT_RECOMMENDATION)

    def _build_prompt(self, profile, query):
        return f"""
        You are a content strategy expert.

        Business:
        Name: {profile.name}
        Domain: {profile.domain}
        Industry: {profile.industry}
        Description: {profile.description or "N/A"}

        Query:
        {query.query_text}

        Search Volume:
        {query.estimated_search_volume}

        Difficulty:
        {query.competitive_difficulty}

        Commercial Intent:
        {query.commercial_intent}

        Domain Visible:
        {query.domain_visible}

        Opportunity Score:
        {query.opportunity_score}

        Generate one content recommendation to improve AI search visibility.

        Return only valid JSON:
        {{
            "title": "string",
            "content_type": "blog_post | landing_page | comparison_page | guide",
            "priority": "high | medium | low",
            "rationale": "string",
            "target_keywords": ["string"]
        }}
        """