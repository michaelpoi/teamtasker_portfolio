import uuid
from django.db import models
from django.db import models
from django.contrib.auth.models import User


# class CustomUser(models.Model):
#     user_id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, null=False)
#     name = models.CharField(max_length=20)
#     email = models.EmailField(max_length=40, unique=True)
#     username = models.CharField(max_length=20, unique=True)
class Project(models.Model):
    project_id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, null=False)
    name = models.CharField(max_length=100)
    desc = models.TextField()
    # creator = models.ForeignKey(User, on_delete=)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'projects'


class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    modify_users = models.BooleanField()
    modify_tasks = models.BooleanField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'role'


class WorkFor(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    is_admin = models.BooleanField()
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('user_id', 'project_id'))
        db_table = 'work_for'


class Task(models.Model):
    task_id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, null=False)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=40)
    desc = models.TextField()
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tasks'


# Create your models here.

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_to')
    created_at = models.DateTimeField(auto_now=True)
    is_read = models.BooleanField(default=False)

    def read(self):
        self.is_read = True
        self.save()

    class Meta:
        abstract = True


class InviteRequest(Notification):
    id = models.AutoField(primary_key=True)
    user_from = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_from')
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def accept(self):
        link = WorkFor(user_id=self.user, project_id=self.project, role=self.role, is_admin=False)
        link.save()
        self.delete()

    def reject(self):
        self.delete()

    class Meta:
        db_table = 'invites'
