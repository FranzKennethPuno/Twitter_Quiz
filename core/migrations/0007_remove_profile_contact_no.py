# Generated by Django 5.1.1 on 2024-10-19 03:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_profile_contact_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='contact_no',
        ),
    ]
