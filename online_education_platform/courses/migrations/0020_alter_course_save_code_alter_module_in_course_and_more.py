# Generated by Django 5.0.7 on 2024-07-28 08:28

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0019_alter_course_save_code_alter_module_in_course_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='save_code',
            field=models.CharField(default=uuid.UUID('a3b9287a-be0e-42c1-b4b8-68a94945f885'), editable=False, max_length=60),
        ),
        migrations.AlterField(
            model_name='module',
            name='in_course',
            field=models.CharField(default=uuid.UUID('a3b9287a-be0e-42c1-b4b8-68a94945f885'), max_length=60),
        ),
        migrations.AlterField(
            model_name='module',
            name='save_code_module',
            field=models.CharField(default=uuid.UUID('3711d1b4-1b66-4bf7-ae5e-750eb5bda901'), editable=False, max_length=60),
        ),
        migrations.AlterField(
            model_name='solution',
            name='for_task',
            field=models.CharField(default=uuid.UUID('31575479-6620-4de6-9e44-081c0dadfa9a'), max_length=60),
        ),
        migrations.AlterField(
            model_name='solution',
            name='solution_code',
            field=models.CharField(default='56549566625804585651264', editable=False, max_length=60, unique=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='in_module',
            field=models.CharField(default=uuid.UUID('3711d1b4-1b66-4bf7-ae5e-750eb5bda901'), max_length=60),
        ),
        migrations.AlterField(
            model_name='task',
            name='save_code_task',
            field=models.CharField(default=uuid.UUID('31575479-6620-4de6-9e44-081c0dadfa9a'), editable=False, max_length=60),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_file',
            field=models.FileField(default=None, upload_to=''),
        ),
    ]
