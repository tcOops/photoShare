from django.db import models

# Create your models here.
class User(models.Model):
	alias = models.CharField(max_length=128)
	name = models.CharField(max_length=128)
	password = models.CharField(max_length=128)
	createTime = models.CharField(max_length=128)
	is_deleted = models.BooleanField(default=False)


class Photo(models.Model):
	name = models.CharField(max_length=128)
	ownerId = models.IntegerField() #0 means owner is public 
	filePath = models.CharField(max_length=128)
	createTime = models.CharField(max_length=128)
	photoSetId = models.IntegerField()
	remark = models.CharField(max_length=300)
	is_deleted = models.BooleanField(default=False)


class PhotoSet(models.Model):
	name = models.CharField(max_length=128)
	ownerId = models.IntegerField()
	isPublic = models.BooleanField()
	isPrivate = models.BooleanField()
	is_deleted = models.BooleanField(default=False)
	remark = models.CharField(max_length=300)
	createTime = models.CharField(max_length=128)