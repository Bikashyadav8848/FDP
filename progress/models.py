from django.db import models
from datetime import date, timedelta

from students.models import Student


def get_week_start(any_date: date) -> date:
    """Return the Monday for the week containing the given date."""
    return any_date - timedelta(days=any_date.weekday())


class Task(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="progress_tasks")
    week_start = models.DateField(help_text="The Monday of the week this task belongs to")
    day = models.DateField(
        null=True,
        blank=True,
        help_text="The specific day this task is assigned to (within the week).",
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-week_start", "day", "title"]
        unique_together = ("student", "day", "title")

    def __str__(self):
        return f"{self.student.name} | {self.day or self.week_start} | {self.title}"
