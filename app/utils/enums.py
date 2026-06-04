from enum import Enum

class LLMResponseType(str, Enum):
    QUERY_DISCOVERY = "query_discovery"
    VISIBILITY_SCORING = "visibility_scoring"
    CONTENT_RECOMMENDATION = "content_recommendation"
