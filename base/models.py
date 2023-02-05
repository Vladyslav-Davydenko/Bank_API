from django.db import models
import uuid
from django.core.validators import MinValueValidator, MaxValueValidator

PERCENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(100)]


class Bank(models.Model):
    name = models.CharField(max_length=255)
    commission = models.DecimalField(max_digits=3, decimal_places=0, default=0, validators=PERCENTAGE_VALIDATOR)

    def __str__(self) -> str:
        return self.name

class Profile(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    bank = models.ForeignKey(Bank, on_delete=models.SET_NULL, null=True)
    balance = models.IntegerField(default=0)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)


    def __str__(self) -> str:
        return f"{self.name} {self.surname}"
