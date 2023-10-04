# base/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SecretSerializer
from .services.secret_service import SecretService
from .exceptions.secret_exceptions import SecretNotFoundError, SecretExpiredError, SecretUnavailableError, InvalidSecretDataError
import logging

logger = logging.getLogger(__name__)
class SecretRetrieveView(APIView):
    def get(self, request, hash):
        try:
            secret_data = SecretService.retrieve_secret(hash)
            return Response(secret_data, status=status.HTTP_200_OK)
        except InvalidSecretDataError as e:
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except SecretNotFoundError as e:
            return Response({'detail': str(e)}, status=status.HTTP_404_NOT_FOUND)
        except SecretExpiredError as e:
            return Response({'detail': str(e)}, status=status.HTTP_410_GONE)
        except SecretUnavailableError as e:
            return Response({'detail': str(e)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.error(e, exc_info=True)
            return Response({'detail': 'An unexpected error occurred.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class SecretCreateView(APIView):
    def post(self, request):
        serializer = SecretSerializer(data=request.data)
        if serializer.is_valid():
            secret_data = SecretService.create_secret(serializer.validated_data)
            return Response(secret_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
