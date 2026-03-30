#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_management.settings')
django.setup()

from students.models import Student
from teachers.models import Teacher
from classes.models import Class
from subjects.models import Subject
from attendance.models import Attendance
from timetable.models import TimeSlot, TimetableEntry
from fees.models import FeeCategory, FeeStructure, StudentFee, FeePayment
from exams.models import Marks

print('=== DATABASE SUMMARY ===')
print(f'Students: {Student.objects.count()}')
print(f'Teachers: {Teacher.objects.count()}')
print(f'Classes: {Class.objects.count()}')
print(f'Subjects: {Subject.objects.count()}')
print(f'Attendance Records: {Attendance.objects.count()}')
print(f'Time Slots: {TimeSlot.objects.count()}')
print(f'Timetable Entries: {TimetableEntry.objects.count()}')
print(f'Fee Categories: {FeeCategory.objects.count()}')
print(f'Fee Structures: {FeeStructure.objects.count()}')
print(f'Student Fees: {StudentFee.objects.count()}')
print(f'Fee Payments: {FeePayment.objects.count()}')
print(f'Marks Records: {Marks.objects.count()}')
print()
print('=== FEE CATEGORIES ===')
for cat in FeeCategory.objects.all():
    print(f'- {cat.name}')
