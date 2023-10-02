# base/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SecretSerializer
from .services.secret_service import SecretService
from .exceptions.secret_exceptions import SecretNotFoundError, SecretExpiredError, SecretUnavailableError

class SecretRetrieveView(APIView):
    def get(self, hash):
        try:
            secret_data = SecretService.retrieve_secret(hash)
            return Response(secret_data, status=status.HTTP_200_OK)
        except SecretNotFoundError:
            return Response({'detail': 'Secret not found.'}, status=status.HTTP_404_NOT_FOUND)
        except SecretExpiredError:
            return Response({'detail': 'Secret has expired.'}, status=status.HTTP_410_GONE)
        except SecretUnavailableError:
            return Response({'detail': 'Secret is no longer available.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'detail': 'An unexpected error occurred.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SecretCreateView(APIView):
    def post(self, request):
        serializer = SecretSerializer(data=request.data)
        if serializer.is_valid():
            secret_data = SecretService.create_secret(serializer.validated_data)
            return Response(secret_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
