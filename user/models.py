from django.db import models
from django.utils.timezone import now

# Create your models here
class Users(models.Model):
    username=models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=16)
    phone=models.CharField(max_length=15)
    created_date=models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table='users'
    def __str__(self):
        return self.username
    