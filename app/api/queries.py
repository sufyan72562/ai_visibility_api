from flask import Blueprint, jsonify

queries_bp = Blueprint("queries", __name__)


@queries_bp.get("/health")
def health_check():
    return jsonify({"status": "ok", "module": "queries"})