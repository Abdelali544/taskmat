from django.contrib import admin
from django.urls import path,include
from todolist_app.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('account',include('users_app.urls')),
    path('todolist/',include('todolist_app.urls'))
]
