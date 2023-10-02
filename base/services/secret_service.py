# base/secret_service.py
from datetime import timedelta
from django.utils import timezone
from ..models import Secret
from ..serializers import SecretSerializer
from ..exceptions.secret_exceptions import SecretNotFoundError, SecretExpiredError, SecretUnavailableError, InvalidSecretDataError


class SecretService:
    @staticmethod
    def retrieve_secret(hash: str):
        try:
            secret = Secret.objects.get(hash=hash)
        except Secret.DoesNotExist:
            raise SecretNotFoundError("The requested secret could not be found in the system.")

        if secret.expires_at and secret.expires_at < timezone.now():
            raise SecretExpiredError("The requested secret has surpassed its time-to-live and has expired.")

        if secret.remaining_views <= 0:
            raise SecretUnavailableError(
                "The requested secret has been viewed the maximum number of allowable times and is no longer available.")

        secret.remaining_views -= 1
        secret.save()

        return SecretSerializer(secret).data

    @staticmethod
    def create_secret(validated_data: dict):
        expire_after = validated_data.pop('expireAfter', 0)
        expires_at = None
        if expire_after > 0:
            expires_at = timezone.now() + timedelta(minutes=expire_after)

        try:
            secret = Secret.objects.create(expires_at=expires_at, **validated_data)
            return SecretSerializer(secret).data
        except SomeBusinessLogicError as e:  # Replace with actual exception you need to handle
            raise InvalidSecretDataError(str(e))