# Generated by Django 5.0.3 on 2024-03-11 13:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 11, 13, 16, 34, 808949, tzinfo=datetime.timezone.utc)),
        ),
    ]