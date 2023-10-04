# base/secret_service.py
from datetime import timedelta
from django.utils import timezone
from ..models import Secret
from ..serializers import SecretSerializer
from ..exceptions.secret_exceptions import SecretNotFoundError, SecretExpiredError, SecretUnavailableError, InvalidSecretDataError
from .hash_validator import is_valid_uuid
class SecretService:

    @staticmethod
    def retrieve_secret(hash: str):
        if not is_valid_uuid(hash):
            raise InvalidSecretDataError()
        try:
            secret = Secret.objects.get(hash=hash)
        except Secret.DoesNotExist:
            raise SecretNotFoundError()
        if secret.expires_at and secret.expires_at < timezone.now():
            raise SecretExpiredError()

        if secret.remaining_views <= 0:
            raise SecretUnavailableError()

        secret.remaining_views -= 1
        secret.save()

        return SecretSerializer(secret).data

    @staticmethod
    def create_secret(validated_data: dict):
        expire_after = validated_data.pop('expireAfter', 0)
        expire_after_views = validated_data.pop('expireAfterViews', 3)
        expires_at = None
        if expire_after > 0:
            expires_at = timezone.now() + timedelta(minutes=expire_after)
        secret = Secret.objects.create(expires_at=expires_at, remaining_views=expire_after_views, **validated_data)
        return SecretSerializer(secret).data

