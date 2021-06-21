
from django.db import models
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from Blog.models import *
from Blog.contactforms import *
# Create your views here.
def register(request):
      if request.method=="POST":
            form=UserRegisterForm(request.POST)
            if form.is_valid():
                  username=form.cleaned_data.get('username')
                  messages.success(request,'Your Account created Now you can login {}!'.format(username))
                  form.save()
                  return redirect('login')
      else:
            form=UserRegisterForm()
      return render(request,'users/register.html',{"form":form})
@login_required
def profile(request):
      data=blog.objects.raw('select * from blog_blog where author_id={}'.format(request.user.id))
      data1=confession.objects.raw('select * from blog_confession where writter_id={}'.format(request.user.id))
      user_blog={
            'user_blog':data,'user_confession':data1
      }
      
      return render(request,'users/profile.html',user_blog)

def edit(request,id):
      data=blog.objects.get(id=id)
      form=blogform(instance=data)
      if request.method=='POST':
            form=blogform(request.POST,request.FILES,instance=data)
            if form.is_valid:
                  form.save()
                  return redirect('profile')
      context={
            'form':form
      }
      return render(request,'users/edit.html',context)

def edit_confession(request,id):
      data=confession.objects.get(id=id)
      form=confessionform(instance=data)
      if request.method=='POST':
            form=confessionform(request.POST,request.FILES,instance=data)
            if form.is_valid:
                  form.save()
                  return redirect('profile')
      context={
            'form':form
      }
      return render(request,'users/edit.html',context)

def delete(request,id):
      data=blog.objects.get(id=id)
      data.delete()
      return redirect('profile')

def delete_conf(request,id):
      data=confession.objects.get(id=id)
      data.delete()
      return redirect('profile')