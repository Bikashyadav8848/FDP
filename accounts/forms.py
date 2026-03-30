from django import forms
from .models import SystemSettings

class SystemSettingsForm(forms.ModelForm):
    class Meta:
        model = SystemSettings
        fields = [
            'institution_name', 
            'academic_year', 
            'official_email', 
            'institution_address',
            'enable_student_portal', 
            'automated_email_notifications', 
            'maintenance_mode',
            'theme_color',
            'notify_absences',
            'notify_fee_dues',
            'notify_exam_results',
            'session_timeout',
            'enforce_strong_passwords',
            'auto_backup_enabled',
            'backup_frequency'
        ]
