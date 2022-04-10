
from email import message
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from users_app.forms import Register_form
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate



# Create your views here.
def register(request):
    if request.method=='POST':
        form=Register_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,('new user added'))
            
            return redirect('todolist')
    else:
        form=Register_form()
        return render(request,'register.html',{'form':form})

# def login_user(request):
#     if request.method=='POST':
#         usenam=request.POST.get('username')
#         password1=request.POST.get('password1')
#         user=authenticate(request,username=usenam,password=password1)
#         if not user==None:
#             login(request,user)
#             return redirect('home')
#         else:
#             messages.success(request,('username or mot de passe incorrect'))

#     return render(request,'login.html')
