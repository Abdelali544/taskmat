
from django.urls import path,include
from .views import todolist,contact,about,delete_task,edit_task,completed_task,pending_task

urlpatterns = [
  
    path('',todolist,name="todolist"),
    path('contact',contact,name="contact"),
    path('about',about,name="about"),
    path('delet/<int:id>',delete_task,name='delete_task'),
    path('edit/<int:id>',edit_task,name='edit_task'),
    path('completed/<int:id>',completed_task,name='completed_task'),
    path('pending/<int:id>',pending_task,name='pendingd_task'),
]
