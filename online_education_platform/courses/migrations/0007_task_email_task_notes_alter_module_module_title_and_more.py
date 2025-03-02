# Generated by Django 5.0.7 on 2024-07-25 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_remove_task_task_module_task_task_module'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='notes',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='module',
            name='module_title',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_description',
            field=models.TextField(blank=True),
        ),
    ]
