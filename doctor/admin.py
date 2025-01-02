from django.contrib import admin
from .models import Doctor, Contact, Availability

class AvailabilityInline(admin.TabularInline):
    model = Availability
    extra = 1  # Number of empty availability rows to display by default

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialty', 'location', 'contact')  # Columns to display in the list view
    search_fields = ('name', 'specialty', 'location')  # Search fields
    inlines = [AvailabilityInline]  # To add Availability directly within Doctor's admin page

class ContactAdmin(admin.ModelAdmin):
    list_display = ('phone', 'email')  # Display phone and email in the list view
    search_fields = ('phone', 'email')  # Search fields

class AvailabilityAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'day', 'time')  # Display doctor, day, and time in the list view
    search_fields = ('doctor__name', 'day', 'time')  # Search fields

# Register models with the admin site
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Availability, AvailabilityAdmin)
