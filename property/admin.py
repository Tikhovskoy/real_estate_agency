from django.contrib import admin
from .models import Flat, Complaint

class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owner']
    readonly_fields = ['created_at']
    list_display = ['address', 'price', 'new_building', 'construction_year', 'town'] 
    list_editable = ['new_building']
    list_filter = ['new_building', 'town', 'active', 'has_balcony', 'construction_year']

class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat',) 
    list_display = ['user', 'flat', 'complaint_text', 'created_at'] 
    search_fields = ['user__username', 'flat__address', 'complaint_text']

admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
