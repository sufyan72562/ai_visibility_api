from flask import Blueprint, jsonify, request

from app.schemas.profile import CreateProfileSchema, ProfileResponseSchema
from app.services.profile_service import ProfileService

profiles_bp = Blueprint("profiles", __name__)


@profiles_bp.post("")
def create_profile():
    try:
        payload = CreateProfileSchema(**request.get_json())

    except Exception as e:
        return jsonify({"error": "Invalid request"}), 400

    try:
        profile = ProfileService.create(payload.model_dump())
    except Exception as e:
        return jsonify({"error": f"Failed to create profile: {str(e)}"}), 500

    response = ProfileResponseSchema.model_validate(profile, from_attributes=True)
    return jsonify(response.model_dump(mode="json")), 201


@profiles_bp.get("/<profile_uuid>")
def get_profile(profile_uuid):
    try:
        profile = ProfileService.get_by_uuid(profile_uuid)
        if not profile:
            return jsonify({"error": "Profile not found"}), 404

        response = ProfileResponseSchema.model_validate(profile, from_attributes=True)
        return jsonify(response.model_dump(mode="json"))
    except Exception as e:
        return jsonify({"error": f"Failed to fetch profile: {str(e)}"}), 500