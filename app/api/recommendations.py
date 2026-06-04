from flask import Blueprint, jsonify

from app.schemas.recommendation import RecommendationResponseSchema
from app.services.recommendation_service import RecommendationService

recommendations_bp = Blueprint("recommendations", __name__)


@recommendations_bp.get("/profiles/<profile_uuid>")
def list_profile_recommendations(profile_uuid):
    try:
        recommendations = RecommendationService.list_by_profile(profile_uuid)
    except ValueError as exc:
        return jsonify({"message": str(exc)}), 404

    return jsonify({
        "data": [
            RecommendationResponseSchema.model_validate(item).model_dump(mode="json")
            for item in recommendations
        ]
    }), 200