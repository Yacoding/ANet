from django.contrib import admin
from blog.models import Posts, Category


class PostsAdmin(admin.ModelAdmin):
	fields = ['title','slug','category','author','excerpt','content', 'public_status','comment_status']
	list_display = ('title','author','post_time','update_time','public_status','comment_status')
	prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
	fields = ['title','slug']
	list_display = ('title','slug')
	prepopulated_fields = {'slug': ('title',)}

admin.site.register(Posts, PostsAdmin)
admin.site.register(Category, CategoryAdmin)