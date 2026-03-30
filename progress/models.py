from django.db import models
from datetime import date, timedelta

from students.models import Student


def get_week_start(any_date: date) -> date:
    """Return the Monday for the week containing the given date."""
    return any_date - timedelta(days=any_date.weekday())


class Task(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('urgent', 'Urgent'),
    ]
    
    CATEGORY_CHOICES = [
        ('academic', 'Academic'),
        ('personal', 'Personal'),
        ('extracurricular', 'Extracurricular'),
        ('health', 'Health'),
        ('other', 'Other'),
    ]
    
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="progress_tasks")
    week_start = models.DateField(help_text="The Monday of the week this task belongs to")
    day = models.DateField(
        null=True,
        blank=True,
        help_text="The specific day this task is assigned to (within the week).",
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='academic')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-week_start", "day", "title"]
        unique_together = ("student", "day", "title")

    def __str__(self):
        return f"{self.student.name} | {self.day or self.week_start} | {self.title}"
    
    @property
    def priority_color(self):
        return {
            'low': 'secondary',
            'medium': 'info',
            'high': 'warning',
            'urgent': 'danger'
        }.get(self.priority, 'secondary')
    
    @property
    def category_icon(self):
        return {
            'academic': 'fas fa-book',
            'personal': 'fas fa-user',
            'extracurricular': 'fas fa-futbol',
            'health': 'fas fa-heartbeat',
            'other': 'fas fa-tasks'
        }.get(self.category, 'fas fa-tasks')
