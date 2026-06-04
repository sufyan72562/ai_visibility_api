from flask import Flask

from app.config import Config
from app.extensions import db, migrate, swagger


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    swagger.init_app(app)

    from app import models  # noqa: F401

    from app.api.profiles import profiles_bp
    from app.api.pipeline import pipeline_bp
    from app.api.queries import queries_bp
    from app.api.recommendations import recommendations_bp

    app.register_blueprint(profiles_bp, url_prefix="/api/v1/profiles")
    app.register_blueprint(pipeline_bp, url_prefix="/api/v1")
    app.register_blueprint(queries_bp, url_prefix="/api/v1/queries")
    app.register_blueprint(recommendations_bp, url_prefix="/api/v1/recommendations")

    return app