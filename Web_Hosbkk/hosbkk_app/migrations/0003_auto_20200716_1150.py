# Generated by Django 3.0 on 2020-07-16 04:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hosbkk_app', '0002_auto_20200716_1149'),
    ]

    operations = [
        migrations.RenameField(
            model_name='case',
            old_name='service_id',
            new_name='service',
        ),
    ]