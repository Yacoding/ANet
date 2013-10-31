#-*-coding:utf8-*-
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

'''文章分类模块'''
class Category(models.Model):
	title = models.CharField(max_length=100)
	slug = models.SlugField(max_length=100)

	def __unicode__(self):
		return self.title

	@models.permalink
	def get_absolute_url(self):
		return('view_blog_category', None, {'slug':self.slug})


class Posts(models.Model):
	content = models.TextField()
	excerpt = models.TextField()
	title   = models.CharField(max_length=100)
	public_status = models.BooleanField()
	comment_status = models.BooleanField()
	post_time = models.DateTimeField(auto_now_add=True)
	update_time = models.DateTimeField(auto_now=True)
	author = models.ForeignKey(User)
	category = models.ForeignKey(Category)
	slug = models.SlugField(max_length=100)

	def __unicode__(self):
		return self.title

	class Meta():
		ordering = ['-post_time']

	@models.permalink
	def get_absolute_url(self):
		return ('view_blog_post', None, {'slug':self.slug})



