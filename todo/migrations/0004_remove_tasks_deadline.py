# Generated by Django 3.2.9 on 2021-12-13 04:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_tasks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasks',
            name='deadline',
        ),
    ]