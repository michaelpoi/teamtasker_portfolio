from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from account.models import Project, Task, Role ,Notification, InviteRequest
from account.models import WorkFor
@login_required
def dashboard(request):
    projects = Project.objects.filter(workfor__user_id=request.user.id).values('project_id',
                                                                               'name',
                                                                               'desc',
                                                                               'start_date',
                                                                               'end_date',
                                                                               'workfor__role__name')
    tasks = Task.objects.none()
    for item in projects:
        role = Role.objects.filter(project_id=item['project_id'], workfor__user_id=request.user).last()
        if role.modify_tasks:
            t = Task.objects.filter(project_id=item['project_id'])
        else:
            t = Task.objects.filter(project_id=item['project_id'], role_id__name=item['workfor__role__name'])
        tasks = tasks.union(t)
    print(tasks)
    #tasks = Task.objects.filter(project_id__workfor__user_id=request.user.id) #should be also filtered by role
    notification_num = InviteRequest.objects.filter(user_id=request.user.id).count()
    return render(request,'dashboard.html', context={'projects':projects, 'tasks':tasks,'n':notification_num})
# Create your views here.
@login_required
def notifications(request):
    for i in InviteRequest.objects.filter(user_id=request.user.id):
        i.read()
    invites = InviteRequest.objects.filter(user_id=request.user.id).values('user_from__username', 'project__name', 'role__name','id')
    return render(request, 'notification.html', {'invites':invites})



@login_required
def accept_invite(request, id):
    invite = get_object_or_404(InviteRequest, id = id)
    invite.accept()
    return redirect('dashboard')


def reject_invite(request, id):
    invite = get_object_or_404(InviteRequest, id=id)
    invite.reject()
    return redirect('dashboard')