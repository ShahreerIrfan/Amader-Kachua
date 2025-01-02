from django.contrib import admin
from .models import FireStation

@admin.register(FireStation)
class FireStationAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'phone', 'mobile')
    search_fields = ('name', 'location')
    list_filter = ('location',)
