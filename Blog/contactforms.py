from django import forms
from django.contrib.auth.models import User
from .models import contact,blog,confession

class contactform(forms.ModelForm):
      class Meta:
            model=contact
            fields="__all__"

class blogform(forms.ModelForm):
      class Meta:
            model=blog
            fields=['title','blog_img','content']

class confessionform(forms.ModelForm):
      class Meta:
            model=confession
            fields=['title','conf_img','content']
      
      
