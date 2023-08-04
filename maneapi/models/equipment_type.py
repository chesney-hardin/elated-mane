"""Equipment type class module"""
from django.db import models


class EquipmentType(models.Model):
    """Equipment type model class"""
    label = models.CharField(max_length=50)
