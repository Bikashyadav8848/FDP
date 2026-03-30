from datetime import date, timedelta

from django.db.models import Q
from django.shortcuts import redirect, render

from students.models import Student
from .models import Task


def get_week_start(any_date: date) -> date:
    return any_date - timedelta(days=any_date.weekday())


def student_progress(request):
    # Get all students for selection
    students = Student.objects.all()
    
    # Get selected student
    student_id = request.GET.get('student')
    if student_id:
        try:
            student = Student.objects.get(id=student_id)
        except Student.DoesNotExist:
            student = students.first()
    else:
        student = students.first()
    
    if not student:
        return render(request, "student_progress.html", {"error": "No students exist yet.", "students": students})

    # Always use current week
    today = date.today()
    week_start = get_week_start(today)

    selected_day_str = request.GET.get("day")
    if selected_day_str:
        try:
            selected_day = date.fromisoformat(selected_day_str)
            # Ensure selected day is within current week
            if selected_day < week_start or selected_day > week_start + timedelta(days=6):
                selected_day = today
        except ValueError:
            selected_day = today
    else:
        selected_day = today

    # Ensure the selected day stays within the chosen week range
    if selected_day < week_start or selected_day > week_start + timedelta(days=6):
        selected_day = week_start

    if request.method == "POST":
        # Handle task deletion
        delete_task_id = request.POST.get("delete_task_id")
        if delete_task_id:
            try:
                task_to_delete = Task.objects.get(id=delete_task_id, student=student)
                task_to_delete.delete()
            except Task.DoesNotExist:
                pass
            return redirect(f"{request.path}?student={student.id}&day={selected_day.isoformat()}")

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
        new_category = request.POST.get("new_task_category", "academic")
        new_priority = request.POST.get("new_task_priority", "medium")
        if new_title:
            Task.objects.create(
                student=student,
                week_start=week_start,
                day=selected_day,
                title=new_title,
                category=new_category,
                priority=new_priority,
            )

        return redirect(f"{request.path}?student={student.id}&day={selected_day.isoformat()}")

    # Prepare week navigation (last 6 weeks) - REMOVED
    # weeks = []
    # for i in range(6):
    #     w = current_week - timedelta(weeks=i)
    #     weeks.append({"start": w, "label": w.strftime("%b %d, %Y")})

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

    # Category breakdown
    category_stats = []
    for cat, label in Task.CATEGORY_CHOICES:
        cat_tasks = tasks_week.filter(category=cat)
        cat_total = cat_tasks.count()
        cat_done = cat_tasks.filter(is_done=True).count()
        if cat_total > 0:
            category_stats.append({
                'category': label,
                'icon': Task(category=cat).category_icon,
                'total': cat_total,
                'done': cat_done,
                'progress': int((cat_done / cat_total) * 100)
            })

    # Priority breakdown
    priority_stats = []
    for pri, label in Task.PRIORITY_CHOICES:
        pri_tasks = tasks_week.filter(priority=pri)
        pri_total = pri_tasks.count()
        pri_done = pri_tasks.filter(is_done=True).count()
        if pri_total > 0:
            priority_stats.append({
                'priority': label,
                'color': Task(priority=pri).priority_color,
                'total': pri_total,
                'done': pri_done,
                'progress': int((pri_done / pri_total) * 100)
            })

    month = week_start.month
    year = week_start.year
    monthly_tasks = Task.objects.filter(student=student, week_start__year=year, week_start__month=month)
    total_month = monthly_tasks.count()
    done_month = monthly_tasks.filter(is_done=True).count()
    monthly_progress = int((done_month / total_month) * 100) if total_month else 0

    # Calculate candlestick data for the week
    candlestick_weekly = []
    for i in range(7):
        day_date = week_start + timedelta(days=i)
        day_tasks = Task.objects.filter(student=student, day=day_date)
        total_tasks = day_tasks.count()
        completed_tasks = day_tasks.filter(is_done=True).count()
        
        # For candlestick: [open, high, low, close]
        # We'll use: [0, total_tasks, 0, completed_tasks] to show progress
        candlestick_weekly.append({
            'x': day_date.strftime('%a'),  # Day name
            'o': 0,  # Open (always 0)
            'h': total_tasks,  # High (total tasks)
            'l': 0,  # Low (always 0) 
            'c': completed_tasks  # Close (completed tasks)
        })

    # Calculate candlestick data for the month
    month_start = week_start.replace(day=1)
    month_end = (month_start + timedelta(days=32)).replace(day=1) - timedelta(days=1)
    
    candlestick_monthly = []
    current_week = month_start
    week_num = 1
    
    while current_week <= month_end:
        week_end = min(current_week + timedelta(days=6), month_end)
        week_tasks = Task.objects.filter(
            student=student, 
            day__gte=current_week, 
            day__lte=week_end
        )
        total_tasks = week_tasks.count()
        completed_tasks = week_tasks.filter(is_done=True).count()
        
        candlestick_monthly.append({
            'x': f'Week {week_num}',
            'o': 0,
            'h': total_tasks,
            'l': 0,
            'c': completed_tasks
        })
        
        current_week = week_end + timedelta(days=1)
        week_num += 1

    context = {
        "student": student,
        "students": students,
        "days": days,
        "selected_week": week_start,
        "selected_day": selected_day,
        "tasks": tasks_for_day,
        "weekly_progress": weekly_progress,
        "monthly_progress": monthly_progress,
        "category_stats": category_stats,
        "priority_stats": priority_stats,
        "chart_data": {
            "weekly": {
                "done": done_week,
                "pending": total_week - done_week
            },
            "monthly": {
                "done": done_month,
                "pending": total_month - done_month
            }
        },
        "candlestick_weekly": candlestick_weekly,
        "candlestick_monthly": candlestick_monthly,
    }

    return render(request, "student_progress.html", context)
