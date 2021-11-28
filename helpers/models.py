from django.db import models


class Audit(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ('-created_at',)


class GenericResponse:
    def __init__(self, message=None, data=None):
        self.message = message
        self.data = data
