from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from account.models import Project, WorkFor, Role, Task, InviteRequest
from django.contrib.auth.models import User

from project.forms import ProjectForm, RoleForm, InviteForm


def is_authorized(user, project_id):
    return WorkFor.objects.filter(project_id=project_id, user_id=user.id).exists()


@login_required
# Create your views here.
def project_view(request, project_id):
    project = get_object_or_404(Project, project_id=project_id)
    if not is_authorized(request.user, project_id):
        return redirect('/')
    role = Role.objects.filter(project_id=project_id, workfor__user_id=request.user.id).last()
    users = User.objects.filter(workfor__project_id=project_id).values('username', 'workfor__role__name')
    if role.modify_tasks:
        tasks = Task.objects.filter(project_id=project_id)
    else:
        tasks = Task.objects.filter(project_id=project_id, role=role)
    return render(request, 'project.html', {'project': project, 'role': role, 'users': users, 'tasks': tasks})


@login_required
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save()  # Save the form data to create a new project
            role = Role(project_id=project, name='Creator', modify_tasks=True, modify_users=True)
            role.save()
            link = WorkFor(user_id=request.user, project_id=project, is_admin=True, role=role)
            link.save()
            return redirect('project_detail', project_id=project.project_id)
    else:
        form = ProjectForm()
    return render(request, 'create_project.html', {'form': form})


def is_authorized_to_change_roles(project_id, user):
    pass


@login_required
def modify_roles(request, project_id):
    roles = Role.objects.filter(project_id=project_id)
    if request.method == 'POST':
        form = RoleForm(request.POST)
        if form.is_valid():
            name = form['name'].value()
            modify_users = form['modify_users'].value()
            modify_tasks = form['modify_tasks'].value()
            role = Role(project_id=Project.objects.filter(project_id = project_id).last(), name=name, modify_users=modify_users, modify_tasks=modify_tasks)
            role.save()
            return redirect(request.path)
    else:
        form = RoleForm()

    return render(request, 'modify_roles.html', {'roles':roles, 'form':form})


def add_user(request, project_id):
    if request.method == 'POST':
        form = InviteForm(project_id,request.POST)
        if form.is_valid():
            user = form['user'].value()
            user_from = request.user
            role = Role.objects.filter(role_id=form['role'].value()).last()
            invite = InviteRequest(user_id=user, user_from=user_from, role=role, project_id=project_id)
            invite.save()
            return redirect('project_detail', project_id=project_id)
    else:
        form = InviteForm(project_id)
    return render(request, 'invite_user.html', {'form':form})