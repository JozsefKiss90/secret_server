from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Secret
from .serializers import SecretSerializer
from datetime import timedelta
from django.utils import timezone


class SecretRetrieveView(APIView):

    def get(self, hash):
        try:
            secret = Secret.objects.get(hash=hash)
        except Secret.DoesNotExist:
            return Response({'detail': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)

        if secret.remaining_views <= 0:
            return Response({'detail': 'This secret is no longer available'}, status=status.HTTP_404_NOT_FOUND)

        serializer = SecretSerializer(secret)
        secret.remaining_views -= 1
        secret.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


class SecretCreateView(APIView):

    def post(self, request):
        serializer = SecretSerializer(data=request.data)

        if serializer.is_valid():
            expire_after = serializer.validated_data.pop('expireAfter', 0)
            expires_at = None

            if expire_after > 0:
                expires_at = timezone.now() + timedelta(minutes=expire_after)

            secret = Secret.objects.create(expires_at=expires_at,
                                           **serializer.validated_data)
            return Response(SecretSerializer(secret).data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)