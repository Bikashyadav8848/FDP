from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import TimeSlot, TimetableEntry

class TimeSlotListView(ListView):
    model = TimeSlot
    template_name = 'timeslots.html'
    context_object_name = 'timeslots'

class TimeSlotCreateView(CreateView):
    model = TimeSlot
    template_name = 'timeslot_form.html'
    fields = ['period_name', 'start_time', 'end_time']
    success_url = reverse_lazy('timeslots')

class TimeSlotUpdateView(UpdateView):
    model = TimeSlot
    template_name = 'timeslot_form.html'
    fields = ['period_name', 'start_time', 'end_time']
    success_url = reverse_lazy('timeslots')

class TimeSlotDeleteView(DeleteView):
    model = TimeSlot
    template_name = 'timeslot_confirm_delete.html'
    success_url = reverse_lazy('timeslots')

class TimetableEntryListView(ListView):
    model = TimetableEntry
    template_name = 'timetable.html'
    context_object_name = 'timetable_entries'

    def get_queryset(self):
        queryset = super().get_queryset()
        class_id = self.request.GET.get('class')
        if class_id:
            queryset = queryset.filter(class_section_id=class_id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        from classes.models import Class
        from .models import TimeSlot
        
        context['classes'] = Class.objects.all()
        context['time_slots'] = TimeSlot.objects.all().order_by('start_time')
        context['days'] = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
        
        # Create a dictionary to easily access entries by time_slot and day
        timetable_dict = {}
        for entry in context['timetable_entries']:
            key = f"{entry.time_slot.id}_{entry.day_of_week}"
            if key not in timetable_dict:
                timetable_dict[key] = []
            timetable_dict[key].append(entry)
        
        context['timetable_dict'] = timetable_dict
        return context

class TimetableEntryCreateView(CreateView):
    model = TimetableEntry
    template_name = 'timetable_form.html'
    fields = ['day_of_week', 'time_slot', 'subject', 'class_section', 'teacher', 'room']
    success_url = reverse_lazy('timetable')

class TimetableEntryUpdateView(UpdateView):
    model = TimetableEntry
    template_name = 'timetable_form.html'
    fields = ['day_of_week', 'time_slot', 'subject', 'class_section', 'teacher', 'room']
    success_url = reverse_lazy('timetable')

class TimetableEntryDeleteView(DeleteView):
    model = TimetableEntry
    template_name = 'timetable_confirm_delete.html'
    success_url = reverse_lazy('timetable')
