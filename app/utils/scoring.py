def calculate_opportunity_score(
    search_volume: int | None,
    difficulty: int | None,
    commercial_intent: float | None,
    domain_visible: bool,
) -> float:
    search_volume = search_volume or 0
    difficulty = difficulty or 0
    commercial_intent = commercial_intent or 0.0

    volume_score = min(search_volume / 2000, 1.0)
    difficulty_score = 1 - min(difficulty / 100, 1.0)
    visibility_gap_score = 0.0 if domain_visible else 1.0

    score = (
        volume_score * 0.35
        + difficulty_score * 0.25
        + visibility_gap_score * 0.25
        + commercial_intent * 0.15
    )

    return round(score, 2)