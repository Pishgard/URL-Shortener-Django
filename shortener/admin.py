from django.contrib import admin
from .models import Url

@admin.register(Url)
class UrlAdmin(admin.ModelAdmin):
    list_display = ['url', 'slug', 'visit']
    readonly_fields = ['visit']
    list_filter = ['created_at']
    search_fields = ['slug']