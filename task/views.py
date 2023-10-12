import datetime

from django.contrib.auth.decorators import login_required
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from account.models import Task, Role
from task.forms import TaskForm, SolveForm
from task.models import Solution


def is_authorized(user, task):
    pass


@login_required
def task_view(request, task_id, project_id):
    task = get_object_or_404(Task, task_id=task_id)
    role = Role.objects.filter(workfor__project_id=project_id, workfor__user_id=request.user.id).last()
    solutions = Solution.objects.filter(task_id=task_id)
    return render(request, 'task.html', {'task': task, 'role': role, 'solutions': solutions})

@login_required
# Create your views here.
def create_task(request, project_id):
    if request.method == 'POST':
        form = TaskForm(project_id,request.POST)
        if form.is_valid():
            name = form['name'].value()
            desc = form['desc'].value()
            start_date = form['start_date'].value()
            end_date = form['end_date'].value()
            role = form['role'].value()
            task = Task(project_id_id=project_id, name=name, desc=desc, start_date=start_date, end_date=end_date, role_id=role)
            task.save()
            return redirect('project_detail', project_id=project_id)
    else:
        form = TaskForm(project_id)
    return render(request,'create_task.html', {'form':form})


def solve_task(request, project_id, task_id):
    task = get_object_or_404(Task, task_id=task_id)
    if request.method == 'POST':
        form = SolveForm(request.POST, request.FILES)
        if form.is_valid():
            author = request.user
            comments = form['comments'].value()
            content_file = request.FILES['content']
            solution = Solution(task_id=task, author=author, comments=comments, content=content_file,post_date=datetime.datetime.now())
            solution.save()
            return redirect('task_detail', project_id=project_id,task_id=task_id)
        else:
            print(form.errors)
    else:
        form = SolveForm()

    return render(request, 'solve_task.html', {'form':form})