# Generated by Django 3.2.3 on 2021-07-12 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drf', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='snippet',
            name='highlighted',
        ),
        migrations.RemoveField(
            model_name='snippet',
            name='owner',
        ),
    ]
