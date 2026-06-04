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
    profile = ProfileService.get_by_uuid(profile_uuid)

    if not profile:
        return jsonify({
            "message": "Profile not found"
        }), 404

    profile_data = (
        ProfileResponseSchema
        .model_validate(profile)
        .model_dump(mode="json")
    )

    profile_data["summary"] = (
        ProfileService.get_profile_summary(
            profile
        )
    )

    return jsonify(profile_data)