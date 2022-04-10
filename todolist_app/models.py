from asyncio import tasks
import imp
from msilib.schema import tables
from select import select
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TaskList(models.Model):
    manege=models.ForeignKey(User,on_delete=models.CASCADE,related_name='tasks')
    task=models.CharField(max_length=300)
    done=models.BooleanField(default=False)

    def __str__(self):
        return self.task+" "+str(self.done)
    

