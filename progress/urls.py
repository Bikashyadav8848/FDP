from django.urls import path

from . import views

app_name = "progress"

urlpatterns = [
    path("", views.student_progress, name="student_progress"),
]
