from rest_framework import serializers
from .models import Secret

class SecretSerializer(serializers.ModelSerializer):
    expireAfter = serializers.IntegerField(write_only=True, required=False, allow_null=True, default=0)

    class Meta:
        model = Secret
        fields = ['hash', 'secret_text', 'created_at', 'expires_at', 'remaining_views', 'expireAfter']
        read_only_fields = ['hash', 'created_at', 'expires_at', 'remaining_views']

    def validate_secret_text(self, value):
        if value == "":
            raise serializers.ValidationError("Secret text cannot be an empty string.")
        return value