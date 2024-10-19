from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime


User = get_user_model()

class Contact(models.Model):
    contact_no = models.IntegerField(default=None)

    def __str__(self):
        return self.user.username

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')
    backgroundimg = models.ImageField(upload_to='back_images', default='blank-profile-picture.png')
    audio_file = models.FileField(upload_to='audios/', default='blank-background-music.mp3')
    audio_title = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)



    def __str__(self):
        return self.user.username

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    caption = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    no_of_likes = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='post_images')
