# Generated by Django 5.1.1 on 2024-10-19 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='contact_no',
            field=models.IntegerField(default=None),
        ),
    ]
