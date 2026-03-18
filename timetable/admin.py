from django.contrib import admin
from .models import TimeSlot, TimetableEntry

@admin.register(TimeSlot)
class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ['period_name', 'start_time', 'end_time']
    ordering = ['start_time']

@admin.register(TimetableEntry)
class TimetableEntryAdmin(admin.ModelAdmin):
    list_display = ['day_of_week', 'time_slot', 'class_section', 'subject', 'teacher', 'room']
    list_filter = ['day_of_week', 'class_section', 'teacher']
    ordering = ['day_of_week', 'time_slot__start_time']
