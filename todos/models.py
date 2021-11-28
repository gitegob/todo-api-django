from django.db import models
from authentication.models import User

from helpers.models import Audit

# Create your models here.


class Todo(Audit):
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_complete = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.title
