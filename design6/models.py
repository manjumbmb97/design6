# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.utils import timezone
from PIL import Image
from django.core.urlresolvers import reverse
# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	date_of_birth = models.DateTimeField(blank=True, null = True)
	profile_pic = models.ImageField(upload_to='users/%Y/%m/%d', blank = True)

	def __str__(self):
		return '{}\'s Profile'.format(self.user.username)

class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(default=timezone.now)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def get_absolute_url(self):
		return reverse('post_detail', kwargs={'pk': self.pk})

	def __str__(self):
		return self.title

class Comment(models.Model):
	post = models.ForeignKey('design6.Post', related_name='comments')
	author = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.text

class Contact(models.Model): 
	name = models.CharField(max_length=200)
	email = models.EmailField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.name

class Gallery(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	caption = models.TextField()
	image = models.ImageField(upload_to = 'gallery/%Y/%m/%d', default = 'gallery/None/no-img.jpg')
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title