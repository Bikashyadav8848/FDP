from django.contrib import admin

from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("student", "week_start", "day", "title", "category", "priority", "is_done", "created_at")
    list_filter = ("week_start", "is_done", "category", "priority")
    search_fields = ("student__name", "title")
    ordering = ("-week_start",)
    list_editable = ("is_done", "category", "priority")
