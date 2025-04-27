from django  import forms
from .models import Twitter
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TwitterForm(forms.ModelForm):
    class Meta:
        model=Twitter
        fields = ['content','image']

class userRegistration(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields =('username','email','password1','password2')