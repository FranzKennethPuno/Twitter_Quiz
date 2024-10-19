# Generated by Django 5.1.1 on 2024-10-19 02:30

import datetime
import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=100)),
                ('caption', models.TextField()),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('no_of_likes', models.PositiveIntegerField(default=0)),
                ('image', models.ImageField(upload_to='post_images')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_user', models.IntegerField()),
                ('bio', models.TextField(blank=True)),
                ('profileimg', models.ImageField(default='blank-profile-picture.png', upload_to='profile_images')),
                ('backgroundimg', models.ImageField(default='blank-profile-picture.png', upload_to='back_images')),
                ('audio_file', models.FileField(default='blank-background-music.mp3', upload_to='audios/')),
                ('audio_title', models.TextField(blank=True)),
                ('location', models.CharField(blank=True, max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]