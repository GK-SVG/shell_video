from django.db import models
from django.utils.timezone import now

# Create your models here
class Users(models.Model):
    user=models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=16)
    phone=models.CharField(max_length=15)
    last_login=models.DateTimeField(auto_now_add=True)
    mail_validate=models.IntegerField(default=0)
    class Meta:
        db_table='users'
    def __str__(self):
        return self.user
    