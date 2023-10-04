from functools import wraps
from rest_framework import status
from rest_framework.response import Response
from ..exceptions.secret_exceptions import InvalidSecretDataError, SecretNotFoundError, \
    SecretExpiredError, SecretUnavailableError
import logging

def handle_response(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            logging.info(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
            result = func(*args, **kwargs)
            logging.info(f"{func.__name__} returned {result}")
            return result
        except InvalidSecretDataError as e:
            logging.exception("InvalidSecretDataError occurred")
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except SecretNotFoundError as e:
            logging.exception("SecretNotFoundError occurred")
            return Response({'detail': str(e)}, status=status.HTTP_404_NOT_FOUND)
        except SecretExpiredError as e:
            logging.exception("SecretExpiredError occurred")
            return Response({'detail': str(e)}, status=status.HTTP_410_GONE)
        except SecretUnavailableError as e:
            logging.exception("SecretUnavailableError occurred")
            return Response({'detail': str(e)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logging.exception("An unexpected error occurred")
            return Response({'detail': 'An unexpected error occurred.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return wrapper
