from django.contrib import admin
from .models import Tasks


@admin.register(Tasks)
class AdminTasks(admin.ModelAdmin):
    list_display = ['id', 'choose', 'note']
    list_filter = ['choose']
    search_fields = ['choose']
