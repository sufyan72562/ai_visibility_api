
class LLMService:
    def generate_query_json(self, prompt: str):
        """
        Temporary mock response.
        Later this method will call OpenAI.
        """
        return [
            {
                "query": "What is the best SEO content optimization tool?",
                "search_volume": 1200,
                "difficulty": 45,
                "commercial_intent": 0.8,
            },
            {
                "query": "Surfer SEO vs Clearscope",
                "search_volume": 900,
                "difficulty": 55,
                "commercial_intent": 0.9,
            },
            {
                "query": "Best AI SEO tools for agencies",
                "search_volume": 1500,
                "difficulty": 60,
                "commercial_intent": 0.85,
            },
        ]
    
    def generate_visibility_json(self, prompt: str):
        if "visibility evaluator" in prompt:
            return {
                "domain_visible": False,
                "visibility_position": None,
                "ai_response_excerpt": "The AI answer mentions competitors but does not clearly mention the target domain.",
            }

        return [
            {
                "query": "What is the best SEO content optimization tool?",
                "search_volume": 1200,
                "difficulty": 45,
                "commercial_intent": 0.8,
            },
            {
                "query": "Surfer SEO vs Clearscope",
                "search_volume": 900,
                "difficulty": 55,
                "commercial_intent": 0.9,
            },
            {
                "query": "Best AI SEO tools for agencies",
                "search_volume": 1500,
                "difficulty": 60,
                "commercial_intent": 0.85,
            },
        ]