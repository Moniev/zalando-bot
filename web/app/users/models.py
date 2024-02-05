from django.db import models
from django.utils import timezone
from controller.models import User

# Create your models here.
class WebsiteLoginInfo(models.Model):
    id: models.AutoField = models.AutoField(primary_key=True)
    user_id: models.ForeignKey = models.ForeignKey(User, on_delete=models.CASCADE) 
    date_time: models.DateTimeField = models.DateTimeField(default=timezone.now)


class WebsiteLogoutInfo(models.Model):
    id: models.AutoField = models.AutoField(primary_key=True)
    user_id: models.ForeignKey = models.ForeignKey(User, on_delete=models.CASCADE) 
    date_time: models.DateTimeField = models.DateTimeField(default=timezone.now)