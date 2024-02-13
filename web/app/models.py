# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cart(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Cart'


class Creditcard(models.Model):
    credit_card_id = models.CharField()
    cash_left = models.FloatField()
    used = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'CreditCard'


class Item(models.Model):
    cart = models.ForeignKey(Cart, models.DO_NOTHING)
    bought_datetime = models.DateTimeField()
    shipped_datetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Item'


class Login(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING)
    success = models.BooleanField()
    date_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Login'


class Logout(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING)
    success = models.BooleanField()
    date_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Logout'


class Opendrop(models.Model):
    website_id = models.CharField()
    title = models.CharField()
    end_datetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'OpenDrop'


class Operation(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING)
    operation_name = models.CharField()
    success = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'Operation'


class Upcomingdrop(models.Model):
    website_id = models.CharField()
    title = models.CharField()
    open_datetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'UpcomingDrop'


class User(models.Model):
    username = models.CharField()
    password = models.CharField()
    email = models.CharField()
    date_joined = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField()
    first_name = models.CharField(blank=True, null=True)
    last_name = models.CharField(blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    is_staff = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'User'


class Websitelogininfo(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING)
    date_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'WebsiteLoginInfo'


class Websitelogoutinfo(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING)
    date_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'WebsiteLogoutInfo'
