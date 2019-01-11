from django.contrib import admin

# Register your models here.
from dashboard.models import UserDetail, Task

admin.site.register(UserDetail)
admin.site.register(Task)