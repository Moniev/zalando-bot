from django.db import models
from django.utils import timezone
from users.models import User

class Cart(models.Model):
    id: models.AutoField = models.AutoField(primary_key=True)
    user_id: models.ForeignKey = models.ForeignKey(User, on_delete=models.CASCADE)


class Item(models.Model):
    id: models.AutoField = models.AutoField(primary_key=True)
    cart_id: models.ForeignKey = models.ForeignKey(Cart, on_delete=models.CASCADE)
    bought_datetime: models.DateTimeField = models.DateTimeField(default=timezone.now)
    shipped_datetime: models.DateTimeField = models.DateTimeField(default=timezone.now)


class Login(models.Model):
    id: models.AutoField = models.AutoField(primary_key=True)
    user_id: models.ForeignKey = models.ForeignKey(User, on_delete=models.CASCADE)
    success: models.BooleanField = models.BooleanField()
    date_time: models.BooleanField = models.DateTimeField(default=timezone.now)


class Logout(models.Model):
    id: models.AutoField = models.AutoField(primary_key=True)
    user_id: models.ForeignKey = models.ForeignKey(User, on_delete=models.CASCADE)
    success: models.BooleanField = models.BooleanField()
    date_time: models.DateTimeField = models.DateTimeField(default=timezone.now)


class UpcomingDrop(models.Model):
    id: models.AutoField = models.AutoField(primary_key=True)
    website_id: models.IntegerField = models.IntegerField()
    title: models.CharField = models.CharField()
    open_datetime: models.DateTimeField = models.DateTimeField(default=timezone.now)


class OpenDrop(models.Model):
    id: models.AutoField = models.AutoField(primary_key=True)
    website_id: models.IntegerField = models.IntegerField()
    title: models.CharField = models.CharField()
    end_datetime: models.DateField = models.DateField(default=timezone.now)


class CreditCard(models.Model):
    id: models.AutoField = models.AutoField(primary_key=True)
    credit_card_id: models.CharField = models.CharField()
    cash_left: models.FloatField = models.FloatField()
    used: models.BooleanField = models.BooleanField() 


class Operation(models.Model):
    id: models.AutoField = models.AutoField(primary_key=True)
    user_id: models.ForeignKey = models.ForeignKey(User, on_delete=models.CASCADE, db_constraint=False)
    operation_name: models.CharField = models.CharField()
    success: models.BooleanField = models.BooleanField()
