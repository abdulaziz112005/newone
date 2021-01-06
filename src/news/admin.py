from django.contrib import admin
from .models import Category, Articles, Tags

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

class ArticlesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']

class TagsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Articles, ArticlesAdmin)
admin.site.register(Tags, TagsAdmin)

