from dataclasses import field
from xml.parsers.expat import model
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Register_form(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email']