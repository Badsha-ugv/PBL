from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['name','user','category']
    prepopulated_fields = {"slug":('name',)}


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ['name','topic']



admin.site.register(Category)
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title','module']
    prepopulated_fields = {"slug":('title',)}

