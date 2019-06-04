from django.db import models

# Create your models here.

class UserInfo(models.Model):
	user_id = models.CharField(max_length=20, primary_key=True)
	username = models.CharField(max_length=20)
	password = models.CharField(max_length=15)
	def __str__(self):
		return self.username

class VideoInfo(models.Model):
	video_id = models.CharField(max_length=20, primary_key=True)
	location = models.CharField(max_length=20)
	wildlife_species = models.CharField(max_length=20)
	ifProcess = models.BooleanField()
	def __str__(self):
		return self.video_id