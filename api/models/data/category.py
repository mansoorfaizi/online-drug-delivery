from django.db import models
from .base import DataRoot


class Category(DataRoot):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
