# Generated by Django 3.0.8 on 2020-11-27 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0016_slip_client'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slip',
            name='price',
        ),
    ]