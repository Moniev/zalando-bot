# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cart(models.Model):
    user = models.ForeignKey('User', models.CASCADE)

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
    cart = models.ForeignKey(Cart, models.CASCADE)
    bought_datetime = models.DateTimeField()
    shipped_datetime = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'Item'


class Login(models.Model):
    user = models.ForeignKey('User', models.CASCADE)
    success = models.BooleanField()
    date_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Login'


class Logout(models.Model):
    user = models.ForeignKey('User', models.CASCADE)
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
    user_id = models.IntegerField()
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
    nickname = models.CharField()
    password = models.CharField()
    email = models.CharField()
    registration_datetime = models.DateTimeField()
    active = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'User'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'