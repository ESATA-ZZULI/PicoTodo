# Generated by Django 3.2.9 on 2021-12-13 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_remove_tasks_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='content',
            field=models.CharField(max_length=100),
        ),
    ]