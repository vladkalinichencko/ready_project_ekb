from django.db import models
from django.conf import settings


class Courses(models.Model):
    name = models.TextField(null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    duration = models.DateTimeField(null=False, blank=False)
    author = models.TextField(null=False, blank=False)


class Article(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    is_author = models.BooleanField(null=False, blank=False, default=False)

