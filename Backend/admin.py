from django.contrib import admin
from .models import Customers, Contacts, Interactions, Deals


@admin.register(Contacts)
class AdminContacts(admin.ModelAdmin):
    list_display = ['id', 'name', 'NIP_numer', 'phone_number', 'email_address', 'price', 'invoice', 'choose', 'type']
    list_filter = ['name']
    search_fields = ['name']


@admin.register(Customers)
class AdminCustomers(admin.ModelAdmin):
    list_display = ['id', 'choose', 'name', 'phone_number', 'price', 'type']
    list_filter = ['name']
    search_fields = ['name']


@admin.register(Interactions)
class AdminInteractions(admin.ModelAdmin):
    list_display = ['id', 'meeting_type', 'person_customer', 'person_contact', 'meeting', 'note']
    list_filter = ['meeting_type']
    search_fields = ['meeting_type']


@admin.register(Deals)
class AdminDeals(admin.ModelAdmin):
    list_display = ['id', 'choose', 'describe']
    list_filter = ['choose']
    search_fields = ['choose']