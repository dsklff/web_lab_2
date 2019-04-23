from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# class Task_List_Manager(models.Manager):
#     def for_user(self, user):
#         return self.filter(owner=user)

class Task_list(models.Model):
    name = models.CharField(max_length=200)
    # owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    # objects = Task_List_Manager()

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }

# class Task_Manager(models.Manager):
#     def for_user(self, user):
#         return self.filter(owner=user)

class Task(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now)
    due_on = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=200, default="in process...")
    task_list = models.ForeignKey(Task_list, on_delete=models.CASCADE)
    # owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    # objects = Task_Manager()

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'status': self.status
        }

    def to_json_detail(self):
        return {
            'id': self.id,
            'name': self.name,
            'created_at': self.created_at,
            'due_on': self.due_on,
            'status': self.status,
        }
