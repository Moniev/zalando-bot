# Generated by Django 5.0.1 on 2024-02-05 09:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_alter_login_date_time_alter_operation_operation_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditcard',
            name='credit_card_id',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='login',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 5, 10, 30, 20, 665800)),
        ),
        migrations.AlterField(
            model_name='opendrop',
            name='title',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='upcomingdrop',
            name='title',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(),
        ),
    ]