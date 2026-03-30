from django.urls import path
from . import views

urlpatterns = [
    # Time Slots
    path('timeslots/', views.TimeSlotListView.as_view(), name='timeslots'),
    path('timeslots/add/', views.TimeSlotCreateView.as_view(), name='timeslot_add'),
    path('timeslots/<int:pk>/edit/', views.TimeSlotUpdateView.as_view(), name='timeslot_edit'),
    path('timeslots/<int:pk>/delete/', views.TimeSlotDeleteView.as_view(), name='timeslot_delete'),

    # Timetable Entries
    path('', views.TimetableEntryListView.as_view(), name='timetable'),
    path('add/', views.TimetableEntryCreateView.as_view(), name='timetable_add'),
    path('<int:pk>/edit/', views.TimetableEntryUpdateView.as_view(), name='timetable_edit'),
    path('<int:pk>/delete/', views.TimetableEntryDeleteView.as_view(), name='timetable_delete'),
]