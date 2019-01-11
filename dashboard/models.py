from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class UserDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % (self.user)


class Task(models.Model):
    user = models.ForeignKey(UserDetail, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now=True)
    end_date = models.DateTimeField()
    STATUS_CHOICE = (
        (1, 'Completed'),
        (2, 'Pending'),
    )
    status = models.IntegerField(choices=STATUS_CHOICE, default=2)

    def __str__(self):
        return '%s' % (self.name)