from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['roll_number', 'name', 'email']
    ordering = ['roll_number']