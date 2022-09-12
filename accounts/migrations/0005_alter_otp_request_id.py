# Generated by Django 4.0.4 on 2022-09-12 16:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_otp_request_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otp',
            name='request_id',
            field=models.UUIDField(default=uuid.UUID('6333db10-ffa3-47bb-9b72-c8a063a7b7a4'), editable=False),
        ),
    ]
