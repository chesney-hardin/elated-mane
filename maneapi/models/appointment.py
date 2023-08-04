"""Appointment class module"""
from django.db import models


class Appointment(models.Model):
    """Appointment model class"""
    customer = models.ForeignKey("Customer", on_delete=models.CASCADE)
    prepaid = models.BooleanField(default=False)
    appointment_date = models.DateField(auto_now=False, auto_now_add=False)
