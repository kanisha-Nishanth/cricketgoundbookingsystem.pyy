from django import forms
# from django.contrib.models import log
from .models import User
from .models import log,contact

class registration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['Firstname','Lastname','Birthday','Gender','Email','PhoneNumber','Password','RetypePassword']

class LoginForm(forms.ModelForm):
   class Meta:
       model = log
       fields ='__all__'

class ContactForm(forms.ModelForm):
    class Meta:
        model = contact
        fields = '__all__'



# class demoform(forms.ModelForm):
#     class Meta:
#         model=demo
#         fields='__all__'