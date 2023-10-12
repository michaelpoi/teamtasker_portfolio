from django.contrib import admin

from task.models import Solution


class Admin(admin.ModelAdmin):
    pass


admin.site.register(Solution, Admin)
# Register your models here.
