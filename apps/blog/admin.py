from django.contrib import admin
from .models import Food, Comment
# Register your models here.

@admin.register(Food)

class UserAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'food_name',
        'photo',
        'description'
    ]

@admin.register(Comment)
class UserAdmin(admin.ModelAdmin):
    list_display = [
            'id',
            'author',
            'food',
            'text',
            'created',
            'updated'
    ]