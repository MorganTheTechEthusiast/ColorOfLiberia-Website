from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent',)
    search_fields = ('name',)
    list_filter = ('parent',)


@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'category', 'city', 'is_verified', 'created_at')
    search_fields = ('name', 'owner__username', 'city', 'category__name')
    list_filter = ('is_verified', 'category', 'city')
    autocomplete_fields = ('owner', 'category')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(BusinessHour)
class BusinessHourAdmin(admin.ModelAdmin):
    list_display = ('business', 'day', 'open_time', 'close_time')
    list_filter = ('day', 'business')
    search_fields = ('business__name',)


@admin.register(BusinessMedia)
class BusinessMediaAdmin(admin.ModelAdmin):
    list_display = ('business', 'logo', 'is_featured')
    list_filter = ('is_featured',)
    search_fields = ('business__name',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('business', 'user', 'rating', 'is_approved', 'created_at')
    search_fields = ('business__name', 'user__username')
    list_filter = ('rating', 'is_approved', 'created_at')


@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('user', 'business', 'added_at')
    search_fields = ('user__username', 'business__name')
    list_filter = ('added_at',)
