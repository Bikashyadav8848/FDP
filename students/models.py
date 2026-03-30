
from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    roll_number=models.CharField(
        max_length=20, 
        unique=True,
        help_text="Unique roll number used for student identification and sorting"
    )

    class Meta:
        ordering = ['roll_number']

    def __str__(self):
        return f"{self.roll_number} - {self.name}"
