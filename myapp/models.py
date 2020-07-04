from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Course(models.Model):
    name=models.CharField(max_length=200)
    category=models.CharField(max_length=50)
    rate=models.IntegerField(default=5,validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])
    price=models.CharField(max_length=5)