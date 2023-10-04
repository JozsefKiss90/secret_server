class BaseSecretError(Exception):
    """Base class for secret-related errors."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class SecretNotFoundError(BaseSecretError):
    """Raised when a secret is not found."""
    def __init__(self, message="The requested secret does not exist."):
        super().__init__(message)


class SecretUnavailableError(BaseSecretError):
    """Raised when a secret is no longer available."""
    def __init__(self, message="The requested secret has reached its view limit and is no longer available."):
        super().__init__(message)

class SecretExpiredError(BaseSecretError):
    def __init__(self, message="The requested secret has surpassed its time-to-live and has expired."):
        super().__init__(message)


class InvalidSecretDataError(BaseSecretError):
    """Raised when the provided data for creating a secret is invalid."""
    def __init__(self, message="The provided data for creating a secret is invalid."):
        super().__init__(message)
