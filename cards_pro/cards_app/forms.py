from django import forms
from .models import Tweet

#use for create form--
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TweetForm(forms.ModelForm):
    class Meta:
        model=Tweet          
        fields=['text','photo']         #we want to use only two fields --- /use arr coz its manaully create DB
        
# now move on to the views.py ---------


#this functionality use for authintation-------
class UserRegistrationForm(UserCreationForm):
    email=forms.EmailField(required=True)
    class Meta:
        model=User
        fields=('username','email','password1','password2')        #use Tuple coz its built in form/ move to views--
        