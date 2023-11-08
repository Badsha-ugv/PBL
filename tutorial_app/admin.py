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

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        user = request.user

        if user.has_perm('tutorial_app.can_view_own_modules'):
            # If the user has permission to view own modules, return only their modules
            return qs.filter(owner=user)
        else:
            # Otherwise, return all modules
            return qs


admin.site.register(Category)
admin.site.register(Submodule)
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title','submodule']
    prepopulated_fields = {"slug":('title',)}

