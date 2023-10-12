
from django.contrib import admin
from django.contrib import admin
from account.models import Project, Role, Task,InviteRequest
from account.models import WorkFor


class Admin(admin.ModelAdmin):
    pass


admin.site.register(Project, Admin)
admin.site.register(WorkFor, Admin)
admin.site.register(Role, Admin)
admin.site.register(Task, Admin)
admin.site.register(InviteRequest)
# Register your models here.
