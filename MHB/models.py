from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,auto_created=True,blank=False,null=False)
    # following = models.ManyToManyField(User,blank=True,null=False)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    username = models.CharField(max_length=20)
    bio = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    birthday = models.DateField(editable=True)
    avatar = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.Profile.username
        # yield Profile.objects.all
    
    class Meta ():
        ordering = ['-created_at']


class Post (models.Model):
    created_by = models.ForeignKey(Profile, on_delete=models.CASCADE,auto_created=True)
    # liked_by = models.ManyToManyField(Profile,auto_created=True)
    created_at = models.DateTimeField(auto_created=True,auto_now=True)
    content = models.TextField(max_length=255)
    image = models.ImageField(blank=True, null=True)

    class Meta ():
        ordering = ['-created_at']

class Like (models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,auto_created=True)
    liked_by = models.ForeignKey(Profile,on_delete=models.CASCADE,auto_created=True)
    created_at = models.DateTimeField(auto_created=True,auto_now=True)

    class Meta ():
        ordering = ['-created_at']

class Comment (models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,auto_created=True)
    commented_by = models.ForeignKey(Profile,on_delete=models.CASCADE,auto_created=True)
    created_at = models.DateTimeField(auto_created=True,auto_now=True)
    content = models.TextField(max_length=255)
    image = models.ImageField(blank=True, null=True)

    class Meta ():
        ordering = ['-created_at']