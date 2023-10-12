import uuid
from django.contrib.auth.models import User

from django.db import models

from account.models import Task


class Solution(models.Model):
    solution_id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default='deleted')
    comments = models.TextField()
    content = models.FileField(upload_to='uploads/', blank=True)
    post_date = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'solutions'
# Create your models here.
