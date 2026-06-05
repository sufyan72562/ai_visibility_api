
import json
from flask import current_app
from openai import OpenAI
from app.utils.enums import LLMResponseType



class LLMService:
    def __init__(self):
        api_key = current_app.config.get("OPENAI_API_KEY")

        if not api_key:
            raise ValueError("OPENAI_API_KEY is missing")

        self.client = OpenAI(api_key=api_key)
        self.model = current_app.config.get("OPENAI_MODEL", "gpt-4o-mini")

    def generate_json(self, prompt: str, response_type: LLMResponseType):
        response = self.client.chat.completions.create(
            model=self.model,
            temperature=0.2,
            messages=[
                {
                    "role": "system",
                    "content": self._system_prompt(response_type),
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
            response_format={
                "type": "json_schema",
                "json_schema": self._json_schema(response_type),
            },
        )

        content = response.choices[0].message.content

        if not content:
            raise ValueError("Empty response from OpenAI")

        return json.loads(content)

    def _system_prompt(self, response_type: LLMResponseType) -> str:
        common = (
            "You are an expert AI search visibility analyst. "
            "Be precise, practical, and business-focused. "
            "Return only valid JSON matching the provided schema. "
            "Do not include markdown, explanations, or extra text."
        )

        prompts = {
            LLMResponseType.QUERY_DISCOVERY: (
                common
                + " Generate realistic AI-search style user queries for the given business. "
                "Focus on queries people would ask ChatGPT, Gemini, Perplexity, or similar AI assistants. "
                "Prefer commercial, comparison, alternative, and problem-aware queries. "
                "Estimate search volume, difficulty, and commercial intent reasonably if exact data is unavailable."
            ),
            LLMResponseType.VISIBILITY_SCORING: (
                common
                + " Evaluate whether the target business/domain is likely to appear in an AI-generated answer "
                "for the provided query. Consider brand mentions, domain mentions, and likely ranking position. "
                "If visibility is uncertain, be conservative."
            ),
            LLMResponseType.CONTENT_RECOMMENDATION: (
                common
                + " Recommend one practical content asset that can improve AI search visibility for the query. "
                "The recommendation should be actionable, SEO-aware, and aligned with the business."
            ),
        }

        return prompts[response_type]

    def _json_schema(self, response_type: LLMResponseType) -> dict:
        schemas = {
            LLMResponseType.QUERY_DISCOVERY: {
                "name": "query_discovery_response",
                "strict": True,
                "schema": {
                    "type": "object",
                    "properties": {
                        "queries": {
                            "type": "array",
                            "minItems": 10,
                            "maxItems": 20,
                            "items": {
                                "type": "object",
                                "properties": {
                                    "query": {"type": "string"},
                                    "search_volume": {
                                        "type": "integer",
                                        "minimum": 0,
                                    },
                                    "difficulty": {
                                        "type": "integer",
                                        "minimum": 0,
                                        "maximum": 100,
                                    },
                                    "commercial_intent": {
                                        "type": "number",
                                        "minimum": 0,
                                        "maximum": 1,
                                    },
                                },
                                "required": [
                                    "query",
                                    "search_volume",
                                    "difficulty",
                                    "commercial_intent",
                                ],
                                "additionalProperties": False,
                            },
                        }
                    },
                    "required": ["queries"],
                    "additionalProperties": False,
                },
            },
            LLMResponseType.VISIBILITY_SCORING: {
                "name": "visibility_scoring_response",
                "strict": True,
                "schema": {
                    "type": "object",
                    "properties": {
                        "domain_visible": {"type": "boolean"},
                        "visibility_position": {
                            "type": ["integer", "null"],
                            "minimum": 1,
                        },
                        "ai_response_excerpt": {"type": "string"},
                    },
                    "required": [
                        "domain_visible",
                        "visibility_position",
                        "ai_response_excerpt",
                    ],
                    "additionalProperties": False,
                },
            },
            LLMResponseType.CONTENT_RECOMMENDATION: {
                "name": "content_recommendation_response",
                "strict": True,
                "schema": {
                    "type": "object",
                    "properties": {
                        "title": {"type": "string"},
                        "content_type": {
                            "type": "string",
                            "enum": [
                                "blog_post",
                                "landing_page",
                                "comparison_page",
                                "guide",
                                "case_study",
                            ],
                        },
                        "priority": {
                            "type": "string",
                            "enum": ["high", "medium", "low"],
                        },
                        "rationale": {"type": "string"},
                        "target_keywords": {
                            "type": "array",
                            "minItems": 3,
                            "maxItems": 8,
                            "items": {"type": "string"},
                        },
                    },
                    "required": [
                        "title",
                        "content_type",
                        "priority",
                        "rationale",
                        "target_keywords",
                    ],
                    "additionalProperties": False,
                },
            },
        }

        return schemas[response_type]