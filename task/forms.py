from django import forms

from account.models import Task, Role
from task.models import Solution


class TaskForm(forms.ModelForm):
    def __init__(self, project,*args, **kwargs):
        super(TaskForm,self).__init__(*args, **kwargs)
        self.fields['role'].queryset = Role.objects.filter(project_id=project)
    class Meta:
        model = Task
        fields = ['name', 'desc', 'start_date', 'end_date', 'role']


class SolveForm(forms.ModelForm):
    class Meta:
        model = Solution
        fields = ['content', 'comments']