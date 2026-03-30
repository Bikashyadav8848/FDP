from rest_framework import serializers
from .models import TimeSlot, TimetableEntry

class TimeSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSlot
        fields = '__all__'

class TimetableEntrySerializer(serializers.ModelSerializer):
    day_of_week_display = serializers.CharField(source='get_day_of_week_display', read_only=True)
    time_slot_display = serializers.CharField(source='time_slot.__str__', read_only=True)
    subject_name = serializers.CharField(source='subject.name', read_only=True)
    class_section_name = serializers.CharField(source='class_section.__str__', read_only=True)
    teacher_name = serializers.CharField(source='teacher.name', read_only=True)

    class Meta:
        model = TimetableEntry
        fields = '__all__'