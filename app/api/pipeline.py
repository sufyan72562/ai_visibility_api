from flask import Blueprint, jsonify
from app.schemas.pipeline import PipelineRunResponseSchema
from app.services.pipeline_service import PipelineService

pipeline_bp = Blueprint("pipeline", __name__)


@pipeline_bp.post("/profiles/<profile_uuid>/run")
def run_pipeline(profile_uuid):
    try:
        pipeline_run = PipelineService.run(profile_uuid)
    except ValueError as exc:
        return jsonify({"message": str(exc)}), 404

    response = PipelineRunResponseSchema.model_validate(pipeline_run)

    return jsonify({
        "message": "Pipeline executed successfully",
        "data": response.model_dump(mode="json"),
    }), 200