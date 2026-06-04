from flask import Blueprint, jsonify
from flask import request
from app.schemas.query import QueryResponseSchema
from app.services.query_service import QueryService

queries_bp = Blueprint("queries", __name__)


@queries_bp.get("/profiles/<profile_uuid>")
def list_profile_queries(profile_uuid):
    try:
        paginated_queries = QueryService.list_by_profile(
            profile_uuid=profile_uuid,
            min_score=request.args.get("min_score", type=float),
            status=request.args.get("status"),
            page=request.args.get("page", default=1, type=int),
            per_page=request.args.get("per_page", default=20, type=int),
        )

    except ValueError as exc:
        return jsonify({"message": str(exc)}), 400

    return jsonify({
        "data": [
            QueryResponseSchema
            .model_validate(query)
            .model_dump(mode="json")
            for query in paginated_queries.items
        ],
        "meta": {
            "page": paginated_queries.page,
            "per_page": paginated_queries.per_page,
            "total": paginated_queries.total,
            "pages": paginated_queries.pages,
            "has_next": paginated_queries.has_next,
            "has_prev": paginated_queries.has_prev,
        }
    }), 200