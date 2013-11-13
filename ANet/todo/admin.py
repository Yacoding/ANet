from django.contrib import admin
from todo.models import Item, DateTime

class ItemAdmin(admin.ModelAdmin):
	list_display = ['name', 'priority', 'difficulty', 'created', 'done']
	search_fields = ['name']

class ItemInline(admin.TabularInline):
	model = Item

class DateAdmin(admin.ModelAdmin):
	list_display = ['datetime']
	inlines = [ItemInline]

admin.site.register(Item, ItemAdmin)
admin.site.register(DateTime, DateTime)