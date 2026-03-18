from django.contrib import admin

from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("student", "week_start", "title", "is_done", "created_at")
    list_filter = ("week_start", "is_done")
    search_fields = ("student__name", "title")
    ordering = ("-week_start",)
