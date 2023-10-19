from django.contrib import admin
from .models import SendEmail


@admin.register(SendEmail)
class SendEmailAdmin(admin.ModelAdmin):
    list_display = ['id', 'topic', 'text', 'sender', 'recipient']
    search_fields = ['topic']
