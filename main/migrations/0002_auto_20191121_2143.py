# Generated by Django 2.2.7 on 2019-11-21 21:43

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_verified',
            field=models.BooleanField(default=False, verbose_name='verified'),
        ),
        migrations.AddField(
            model_name='user',
            name='verification_uuid',
            field=models.UUIDField(default=uuid.uuid4, verbose_name='Unique Verification UUID'),
        ),
    ]
