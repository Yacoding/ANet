#-*-coding:utf8-*-
from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

'''文章分类模块'''
class Category(models.Model):
	title = models.CharField(max_length=100)
	slug = models.SlugField(max_length=100)
	cat_img = models.ImageField(upload_to="category_icon", blank=True, null=True)

	def __unicode__(self):
		return self.title

	def image_(self):
		return self.cat_img.url

	@models.permalink
	def get_absolute_url(self):
		return('view_blog_category', None, {'slug':self.slug})

'''文章内容'''
class Posts(models.Model):
	#content = models.TextField()
	content = HTMLField()
	excerpt = HTMLField()
	title   = models.CharField(max_length=100)
	#post_image = models.HTMLField(upload_to='article_images/%Y/%m/%d')
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


'''文章评论模块'''
class Comments(models.Model):
	author = models.CharField(max_length=100, blank=True)
	body = HTMLField()
	post = models.ForeignKey(Posts)
	created_time = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return u"%s: %s" %(self.author, self.body[:60])

	class Meta():
		ordering = ['-created_time']