from flask import Blueprint, jsonify

from app.schemas.query import QueryResponseSchema
from app.services.query_service import QueryService

queries_bp = Blueprint("queries", __name__)


@queries_bp.get("/profiles/<profile_uuid>")
def list_profile_queries(profile_uuid):
    try:
        queries = QueryService.list_by_profile(profile_uuid)
    except ValueError as exc:
        return jsonify({"message": str(exc)}), 404

    return jsonify({
        "data": [
            QueryResponseSchema.model_validate(query).model_dump(mode="json")
            for query in queries
        ]
    }), 200