from django.db import models
import uuid

class Secret(models.Model):
    secret_text = models.TextField()
    hash = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(null=True, blank=True)
    remaining_views = models.IntegerField(default=3)
