from flask import Blueprint, jsonify
from app.schemas.profile import CreateProfileSchema, ProfileResponseSchema
from app.services.profile_service import ProfileService
from flask import request

profiles_bp = Blueprint("profiles", __name__)



@profiles_bp.post("")
def create_profile():

    payload = CreateProfileSchema(
        **request.get_json()
    )

    profile = ProfileService.create(
        payload.model_dump()
    )

    response = ProfileResponseSchema.model_validate(
        profile,
        from_attributes=True,
    )

    return jsonify(
        response.model_dump(mode="json")
    ), 201



@profiles_bp.get("/<profile_uuid>")
def get_profile(profile_uuid):

    profile = ProfileService.get_by_uuid(
        profile_uuid
    )

    if not profile:
        return jsonify({
            "message": "Profile not found"
        }), 404

    response = ProfileResponseSchema.model_validate(
        profile,
        from_attributes=True,
    )

    return jsonify(
        response.model_dump(mode="json")
    )