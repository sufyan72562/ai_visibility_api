from flask import Blueprint, jsonify

recommendations_bp = Blueprint("recommendations", __name__)


@recommendations_bp.get("/health")
def health_check():
    return jsonify({"status": "ok", "module": "recommendations"})