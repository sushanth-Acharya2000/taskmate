# Generated by Django 4.2.13 on 2024-05-25 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0002_task_list_manager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task_list',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
