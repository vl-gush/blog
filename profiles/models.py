from django.conf import settings
from django.db import models


class Address(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="addresses",
        blank=True,
        null=True,
    )
    city = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
