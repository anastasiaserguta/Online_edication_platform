# Generated by Django 5.0.7 on 2024-07-24 14:05

from django.db import migrations, models
from uuid import uuid4


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name="Course",
            name="uuid",
            field=models.UUIDField(default=uuid4, null=True),
        ),
    ]
