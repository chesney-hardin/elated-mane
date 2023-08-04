"""Equipment class module"""
from django.db import models
from django.contrib.auth.models import User


class Equipment(models.Model):
    """Equipment model class"""
    stylist = models.ForeignKey(User, on_delete=models.CASCADE, related_name='equipment')
    type = models.ForeignKey("EquipmentType", on_delete=models.CASCADE, related_name='current_equipment')
    manufacturer = models.CharField(max_length=75)
    cost = models.DecimalField(decimal_places=2, max_digits=6)
    purchase_date = models.DateField(auto_now=False, auto_now_add=False)
