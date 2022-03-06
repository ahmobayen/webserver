from django.contrib import admin

# Register your models here.
from django.contrib.admin import display

from .models import Categories, Articles


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("category", "description", )


class ArticlesAdmin(admin.ModelAdmin):
    list_display = ("title", "body", "source", "timestamp", "type", )


admin.site.register(Categories, CategoryAdmin)
admin.site.register(Articles, ArticlesAdmin)
