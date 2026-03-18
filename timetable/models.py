from django.db import models
from subjects.models import Subject
from classes.models import Class
from teachers.models import Teacher

class TimeSlot(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    period_name = models.CharField(max_length=50, help_text="e.g., Period 1, Break, Lunch")

    class Meta:
        ordering = ['start_time']
        verbose_name = 'Time Slot'
        verbose_name_plural = 'Time Slots'

    def __str__(self):
        return f"{self.period_name} ({self.start_time.strftime('%H:%M')} - {self.end_time.strftime('%H:%M')})"

class TimetableEntry(models.Model):
    DAYS_OF_WEEK = [
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
        ('sunday', 'Sunday'),
    ]

    day_of_week = models.CharField(max_length=10, choices=DAYS_OF_WEEK)
    time_slot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    class_section = models.ForeignKey(Class, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    room = models.CharField(max_length=50, blank=True, null=True, help_text="Classroom or room number")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['time_slot__start_time', 'day_of_week']
        verbose_name = 'Timetable Entry'
        verbose_name_plural = 'Timetable Entries'
        unique_together = ['day_of_week', 'time_slot', 'class_section']

    def __str__(self):
        return f"{self.get_day_of_week_display()} - {self.time_slot} - {self.class_section} - {self.subject}"
