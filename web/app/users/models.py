from django.db import models
from django.utils import timezone
from backend.models import User

# Create your models here.
class LoginInfo(models.Model):
    id: models.AutoField = models.AutoField(primary_key=True)
    user_id: models.ForeignKey = models.ForeignKey(User, on_delete=models.CASCADE)
    date_time = models.DateTimeField(default=timezone.now)


class LogoutInfo(models.Model):
    id: models.AutoField = models.AutoField(primary_key=True)
    user_id: models.ForeignKey = models.ForeignKey(User, on_delete=models.CASCADE)
    date_time = models.DateTimeField(default=timezone.now)