
from django.db import models

class Class(models.Model):
    name = models.CharField(max_length=50)
    section = models.CharField(max_length=10)

    class Meta:
        ordering = ['name', 'section']
        verbose_name = 'Class'
        verbose_name_plural = 'Classes'

    def __str__(self):
        return f"{self.name} - {self.section}"
