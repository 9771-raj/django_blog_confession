from django.core import paginator
from django.shortcuts import render,redirect
from .contactforms import contactform,blogform,confessionform
from django.contrib.auth.decorators import login_required
from .models import * 
from django.core.paginator import Paginator
# Create your views here.
def index(request):
      #print(request.user.username)
      form=contactform()
      if request.method=='POST':
            form=contactform(request.POST)
            if form.is_valid:
                  form.save()
                  return redirect('index')
      context={'form':form}
      return render(request,'Blog/index.html',context)
@login_required
def blog_corner(request):
      use_name=request.user.username
      data=blog.objects.all().order_by('-date_blog')
      paginator=Paginator(data,5)    # apply pagination in blog corner
      page_num=request.GET.get('page')
      page_obj=paginator.get_page(page_num)
      blog_data={
            #"blog_data":data
            "blog_data":page_obj
      }
      return render(request,"Blog/blog.html",blog_data)
@login_required
def confession_corner(request):
      use_name=request.user.username
      data=confession.objects.all().order_by('-date_posted')
      paginator=Paginator(data,5)
      page_num=request.GET.get('page')
      page_obj=paginator.get_page(page_num)
      conf_data={
            "conf_data":page_obj
      }
      return render(request,"Blog/confession.html",conf_data)

def add_blog(request):
      print(request.user.id)
      form=blogform(initial={'author':request.user.id})
      if request.method=='POST':
            form=blogform(request.POST,request.FILES)
            if form.is_valid():
                  f=form.save(commit=False)
                  f.author=request.user
                  f.save()
                  return redirect('blog')
            
      context={'form':form}
      return render(request,"Blog/add_blog.html",context)

def add_conf(request):
      form=confessionform(initial={'writter':request.user.id})
      if request.method=='POST':
            form=confessionform(request.POST,request.FILES)
            if form.is_valid():
                  f=form.save(commit=False)
                  f.writter=request.user
                  f.save()
                  return redirect('confession')
            else:
                  form=confessionform()
      context={'form':form}
      return render(request,"Blog/add_conf.html",context)