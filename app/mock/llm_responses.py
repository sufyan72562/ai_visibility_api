QUERY_DISCOVERY_RESPONSE = [
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


VISIBILITY_SCORING_RESPONSE = {
    "domain_visible": False,
    "visibility_position": None,
    "ai_response_excerpt": (
        "The AI answer mentions competitors but does not clearly "
        "mention the target domain."
    ),
}


CONTENT_RECOMMENDATION_RESPONSE = {
    "title": "Best AI SEO Tools for Agencies in 2026",
    "content_type": "blog_post",
    "priority": "high",
    "rationale": (
        "This query has strong commercial intent and the business "
        "is not visible in AI-generated answers."
    ),
    "target_keywords": [
        "AI SEO tools",
        "SEO software for agencies",
        "content optimization tools",
    ],
}