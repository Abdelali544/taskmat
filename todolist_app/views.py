from distutils.errors import LibError
from http.client import HTTPResponse
import imp
from multiprocessing import Manager, context
import re
from site import USER_SITE
from urllib import request
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import TaskList
from .form import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib.auth import login,logout,authenticate
# Create your views here.
from django.contrib.auth.decorators import login_required

def home(request):
    

    
    return render( request,"home.html",)

@login_required(login_url='login')
def todolist(request):
    if request.method=='POST':
        form=TaskForm(request.POST or None)
        if form.is_valid():
            # zid liya user 
            form.save(commit=False).manege=request.user
            form.save()
           
            messages.success(request,("New Task Add"))
            
            return redirect('todolist')
        
    else:
        # folter by user
        all_task=TaskList.objects.filter(manege=request.user)
        
        paginator=Paginator(all_task,10)
        page=request.GET.get('pg')
        all_task=paginator.get_page(page)
        return render(request,'todolist.html',{'all_task':all_task})
@login_required(login_url='home')
def delete_task(request,id):
    task=TaskList.objects.get(id=id)
    task.delete()
    return redirect('todolist')

def completed_task(request,id):
    task=TaskList.objects.get(id=id)
    task.done=True
    task.save()
    return redirect('todolist')

def pending_task(request,id):
    task=TaskList.objects.get(id=id)
    task.done=False
    task.save()
    return redirect('todolist')

def edit_task(request,id):
    task=TaskList.objects.get(id=id)
    if(request.method=='POST'):
        form=TaskForm(request.POST,None,instance=task)
        if form.is_valid():
            form.save()
            messages.success(request,"Task Edited")
            return redirect('todolist')
    else:
        
        return render(request,'edit.html',{'task':task})

def contact(request):
    context={"welcom:welcom text"}
    return render(request,'contact.html')

def about(request):
    context={"welcom:welcom about"}
    return render(request,'about.html') 


