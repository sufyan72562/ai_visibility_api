
from app.mock.llm_responses import (
    QUERY_DISCOVERY_RESPONSE,
    VISIBILITY_SCORING_RESPONSE,
    CONTENT_RECOMMENDATION_RESPONSE,
)

from app.utils.enums import LLMResponseType

class LLMService:
    def generate_json(
        self,
        prompt: str,
        response_type: LLMResponseType,
    ):
        """
        Temporary mocked LLM response handler.
        Later this method will call OpenAI and parse JSON.
        """

        mock_responses = {
            LLMResponseType.QUERY_DISCOVERY: QUERY_DISCOVERY_RESPONSE,
            LLMResponseType.VISIBILITY_SCORING: VISIBILITY_SCORING_RESPONSE,
            LLMResponseType.CONTENT_RECOMMENDATION: CONTENT_RECOMMENDATION_RESPONSE,
        }

        if response_type not in mock_responses:
            raise ValueError(f"Unsupported LLM response type: {response_type}")

        return mock_responses[response_type]