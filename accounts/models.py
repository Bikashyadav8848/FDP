from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=[('student', 'Student'), ('teacher', 'Teacher'), ('admin', 'Admin')])

    def __str__(self):
        return self.user.username

class SystemSettings(models.Model):
    institution_name = models.CharField(max_length=255, default="Excellence High School")
    academic_year = models.CharField(max_length=50, default="2024 - 2025")
    official_email = models.EmailField(default="admin@excellence.edu")
    institution_address = models.TextField(default="123 Education Boulevard, Knowledge City")
    
    # Preferences
    enable_student_portal = models.BooleanField(default=True)
    automated_email_notifications = models.BooleanField(default=True)
    maintenance_mode = models.BooleanField(default=False)

    # Appearance
    theme_color = models.CharField(max_length=20, default="indigo", choices=[('indigo', 'Indigo / Primary'), ('sapphire', 'Sapphire Blue'), ('emerald', 'Emerald Green'), ('slate', 'Slate Dark')])
    
    # Notifications
    notify_absences = models.BooleanField(default=True)
    notify_fee_dues = models.BooleanField(default=True)
    notify_exam_results = models.BooleanField(default=True)

    # Security
    session_timeout = models.IntegerField(default=30)
    enforce_strong_passwords = models.BooleanField(default=False)

    # Backups
    auto_backup_enabled = models.BooleanField(default=True)
    backup_frequency = models.CharField(max_length=20, default="weekly", choices=[('daily', 'Daily'), ('weekly', 'Weekly'), ('monthly', 'Monthly')])

    class Meta:
        verbose_name = "System Settings"
        verbose_name_plural = "System Settings"

    def __str__(self):
        return "Global Settings"

    def save(self, *args, **kwargs):
        # Ensure only one instance of SystemSettings exists
        if self._state.adding and SystemSettings.objects.exists():
            raise ValueError("Only a single SystemSettings instance is allowed")
        super().save(*args, **kwargs)

    @classmethod
    def get_settings(cls):
        # Returns the first instance or creates it if it doesn't exist
        obj, created = cls.objects.get_or_create(id=1)
        return obj