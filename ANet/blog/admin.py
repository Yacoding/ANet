from django.contrib import admin
from blog.models import Posts


class PostsAdmin(admin.ModelAdmin):
	fields = ['title','author','excerpt','content', 'public_status','comment_status']
	list_display = ('title','author','post_time','update_time','public_status','comment_status')
admin.site.register(Posts, PostsAdmin)