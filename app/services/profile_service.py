from app.extensions import db
from app.models.profile import BusinessProfile


class ProfileService:

    @staticmethod
    def create(data):
        profile = BusinessProfile(**data)

        db.session.add(profile)
        db.session.commit()

        return profile

    @staticmethod
    def get_by_uuid(profile_uuid):
        return BusinessProfile.query.filter_by(
            uuid=profile_uuid
        ).first()

    @staticmethod
    def list():
        return BusinessProfile.query.all()