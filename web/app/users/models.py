from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, BaseUserManager
from datetime import datetime

class CustomUserManager(BaseUserManager):
    def create_user(self, username: str, password: str, email: str, **other_fields):
        if not email:
            raise ValueError
        
        user: AbstractUser = self.model(email=self.normalize_email(email), username=username, date_joined=timezone.now())
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username: str, password: str, email: str, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        return self.create_user(username, password, email, **other_fields)
    
    
class User(AbstractUser):
    username = models.CharField(unique=True)
    password = models.CharField(null=False)
    email = models.CharField(unique=True)
    date_joined = models.DateTimeField(null=True)
    last_login = models.DateTimeField(null=True)
    last_name = models.CharField(null=True)
    first_name = models.CharField(null=True)

    USERNAME_FIELD = 'username'

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    class Meta:
        managed = False
        db_table = 'User'

    def __repr__(self):
        return f"[username]: {self.username}, [email]: {self.email}"


class WebsiteLoginInfo(models.Model):
    id: models.AutoField = models.AutoField(primary_key=True)
    user_id: models.ForeignKey = models.ForeignKey(User, on_delete=models.CASCADE) 
    date_time: models.DateTimeField = models.DateTimeField(default=timezone.now)


class WebsiteLogoutInfo(models.Model):
    id: models.AutoField = models.AutoField(primary_key=True)
    user_id: models.ForeignKey = models.ForeignKey(User, on_delete=models.CASCADE) 
    date_time: models.DateTimeField = models.DateTimeField(default=timezone.now)
