from django.db import models
from django.contrib.auth.models import User

class Posts(models.Model):
	content = models.TextField()
	excerpt = models.TextField()
	title   = models.CharField(max_length=100)
	public_status = models.BooleanField()
	comment_status = models.BooleanField()
	post_time = models.DateTimeField(auto_now_add=True)
	update_time = models.DateTimeField(auto_now=True)
	author = models.ForeignKey(User)

