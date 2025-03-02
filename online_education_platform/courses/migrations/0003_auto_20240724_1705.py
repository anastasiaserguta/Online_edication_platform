# Generated by Django 5.0.7 on 2024-07-24 14:05

from django.db import migrations, models
from uuid import uuid4

def gen_uuid(apps, schema_editor):
    MyModel = apps.get_model("myapp", "MyModel")
    for row in MyModel.objects.all():
        row.uuid = uuid4()
        row.save(update_fields=["uuid"])

class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20240724_1705'),
    ]

operations = [
        migrations.RunPython(gen_uuid, reverse_code=migrations.RunPython.noop),
    ]
