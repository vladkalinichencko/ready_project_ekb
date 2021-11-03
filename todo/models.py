from django.db import models


class Todo(models.Model):
    number = models.IntegerField(null=False, blank=False)
    is_done = models.BooleanField(
        null=False,
        blank=False,
        default=False
    )
    text = models.CharField(
        null=False,
        blank=False,
        max_length=256
    )
