# Generated by Django 4.0.3 on 2022-04-13 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='albumphoto',
            name='customer',
        ),
    ]