from django.contrib import admin

from .models import Advertisement
# Register your models here.

@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'creator', 'created_at', 'updated_at')

    actions = ['PATCH', 'DELETE']

    def PATCH(self, request, queryset):
        queryset.update(status='CLOSED' if queryset.filter(status='OPEN').exists() else 'OPEN')

    def DELETE(self, request, queryset):
        queryset.delete()
