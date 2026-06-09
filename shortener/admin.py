from django.contrib import admin

# Register your models here.
from .models import ShortURL

@admin.register(ShortURL)
class ShortURLAdmin(admin.ModelAdmin):
    list_display = ('short_code', 'original_url','click_count', 'created_at')
    search_fields = ('short_code', 'original_url','click_count')
    ordering = ['id']
