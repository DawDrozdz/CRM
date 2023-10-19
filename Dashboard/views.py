from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Tasks
from .forms import TaskForm
from django.contrib.auth.decorators import login_required


@login_required()
def front_page(request):
    task_state = Tasks.objects.filter(choose='STATES').all()
    task_motorcycle = Tasks.objects.filter(choose='MOTORCYCLE').all()
    return render(request, 'front_page.html', {
        'task_state': task_state,
        'task_motorcycle': task_motorcycle,
    })


@login_required()
def edit_task(request, pk):
    edit = get_object_or_404(Tasks, pk=pk)
    edit_tasks = TaskForm(request.POST or None, instance=edit)

    if edit_tasks.is_valid():
        edit_tasks.save()
        messages.success(request, "Task was updated.")
        return redirect(front_page)
    return render(request, 'edit_task.html', {
        'edit_tasks': edit_tasks,
    })
