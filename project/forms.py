from django import forms
from django.contrib.auth.models import User

from account.models import Project, Role, InviteRequest, WorkFor


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'desc', 'start_date', 'end_date']

class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ['name', 'modify_tasks', 'modify_users']



class InviteForm(forms.ModelForm):
    def __init__(self,project_id,*args,**kwargs):
        super(InviteForm, self).__init__(*args, **kwargs)
        self.fields['role'].queryset = Role.objects.filter(project_id=project_id)
    class Meta:
        model = InviteRequest
        fields = ['user', 'role']