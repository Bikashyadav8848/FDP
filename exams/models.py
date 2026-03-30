
from django.db import models
from students.models import Student
from subjects.models import Subject

class Marks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.IntegerField()
    exam_name = models.CharField(max_length=100, default='Exam', help_text="e.g., Mid Term, Final Exam")
    out_of = models.IntegerField(default=100, help_text="Maximum marks")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.student.name} - {self.subject.name} - {self.marks}/{self.out_of}"
