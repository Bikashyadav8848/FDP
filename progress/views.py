from datetime import date, timedelta

from django.db.models import Q
from django.shortcuts import redirect, render

from students.models import Student
from .models import Task


def get_week_start(any_date: date) -> date:
    return any_date - timedelta(days=any_date.weekday())


def student_progress(request):
    # For now, we select the first student (or later extend to auth-based student selection)
    student = Student.objects.first()
    if not student:
        return render(request, "student_progress.html", {"error": "No students exist yet."})

    selected_week_str = request.GET.get("week")
    if selected_week_str:
        try:
            selected_week = date.fromisoformat(selected_week_str)
        except ValueError:
            selected_week = date.today()
    else:
        selected_week = date.today()

    week_start = get_week_start(selected_week)

    selected_day_str = request.GET.get("day")
    if selected_day_str:
        try:
            selected_day = date.fromisoformat(selected_day_str)
        except ValueError:
            selected_day = week_start
    else:
        selected_day = week_start

    # Ensure the selected day stays within the chosen week range
    if selected_day < week_start or selected_day > week_start + timedelta(days=6):
        selected_day = week_start

    if request.method == "POST":
        # Update existing task completion state (handle unchecked boxes too)
        tasks_for_day = Task.objects.filter(
            student=student,
            week_start=week_start,
        ).filter(Q(day=selected_day) | Q(day__isnull=True))

        for task in tasks_for_day:
            # Ensure tasks without a day are assigned to the selected day
            if task.day is None:
                task.day = selected_day

            checkbox_name = f"task_{task.id}"
            is_checked = checkbox_name in request.POST
            if task.is_done != is_checked:
                task.is_done = is_checked

            task.save()

        # Add new task if provided
        new_title = request.POST.get("new_task_title", "").strip()
        new_desc = request.POST.get("new_task_desc", "").strip()
        if new_title:
            Task.objects.create(
                student=student,
                week_start=week_start,
                day=selected_day,
                title=new_title,
                description=new_desc,
            )

        return redirect(f"{request.path}?week={week_start.isoformat()}&day={selected_day.isoformat()}")

    # Prepare week navigation (last 6 weeks)
    today = date.today()
    current_week = get_week_start(today)
    weeks = []
    for i in range(6):
        w = current_week - timedelta(weeks=i)
        weeks.append({"start": w, "label": w.strftime("%b %d, %Y")})

    # Ensure existing tasks without a day are treated as Monday tasks (for backward compatibility)
    Task.objects.filter(student=student, week_start=week_start, day__isnull=True).update(day=week_start)

    # Tasks visible for selected day
    tasks_for_day = Task.objects.filter(student=student, week_start=week_start, day=selected_day).order_by("title")

    # Build day navigation for the current week (Monday - Sunday)
    days = []
    for i in range(7):
        day = week_start + timedelta(days=i)
        days.append({"date": day, "label": day.strftime("%a %d")})

    # Weekly progress calculation (all tasks in week)
    tasks_week = Task.objects.filter(student=student, week_start=week_start)
    total_week = tasks_week.count()
    done_week = tasks_week.filter(is_done=True).count()
    weekly_progress = int((done_week / total_week) * 100) if total_week else 0

    month = week_start.month
    year = week_start.year
    monthly_tasks = Task.objects.filter(student=student, week_start__year=year, week_start__month=month)
    total_month = monthly_tasks.count()
    done_month = monthly_tasks.filter(is_done=True).count()
    monthly_progress = int((done_month / total_month) * 100) if total_month else 0

    chart_data = {
        "weekly": {"done": done_week, "pending": total_week - done_week},
        "monthly": {"done": done_month, "pending": total_month - done_month},
    }

    context = {
        "student": student,
        "weeks": weeks,
        "days": days,
        "selected_week": week_start,
        "selected_day": selected_day,
        "tasks": tasks_for_day,
        "weekly_progress": weekly_progress,
        "monthly_progress": monthly_progress,
        "chart_data": chart_data,
    }

    return render(request, "student_progress.html", context)
