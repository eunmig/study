from django.contrib import admin
from .models import Category, Comment, Post
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment)
admin.site.register(Post)
