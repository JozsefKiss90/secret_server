# base/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .directives.request_directives import handle_response
from .serializers import SecretSerializer
from .services.secret_service import SecretService

class SecretRetrieveView(APIView):
    @handle_response
    def get(self, request, hash):
        secret_data = SecretService.retrieve_secret(hash)
        return Response(secret_data, status=status.HTTP_200_OK)


class SecretCreateView(APIView):
    def post(self, request):
        serializer = SecretSerializer(data=request.data)
        if serializer.is_valid():
            secret_data = SecretService.create_secret(serializer.validated_data)
            return Response(secret_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
