from django.contrib import admin
from .models import Flat, Complaint, Owner


class OwnerInline(admin.TabularInline):
    model = Flat.owners.through
    raw_id_fields = ['owner']


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address']
    readonly_fields = ['created_at']
    list_display = ['address', 'price', 'new_building', 'construction_year', 'town', 'owner_names', 'owner_phones']
    list_editable = ['new_building']
    list_filter = ['new_building', 'town', 'active', 'has_balcony', 'construction_year']
    raw_id_fields = ['likes', 'owners']
    inlines = [OwnerInline]

    def owner_names(self, obj):
        return ', '.join([owner.name for owner in obj.owners.all()])
    owner_names.short_description = 'Владельцы'

    def owner_phones(self, obj):
        return ', '.join([str(owner.pure_phone) for owner in obj.owners.all() if owner.pure_phone])
    owner_phones.short_description = 'Телефоны'


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ['user', 'flat']


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ['name', 'pure_phone']
    search_fields = ['name', 'pure_phone']
    raw_id_fields = ['flats_as_owner']
