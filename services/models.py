from django.db import models

# Create your models here.
class StoreMailVarificatioLink(models.Model):
    token=models.TextField()
    email=models.CharField(max_length=150)
    uid=models.IntegerField()

    class Meta:
        db_table='store_user_mail_valification_link'
    def __str__(self):
        return 'user id ' + str(self.uid)
    