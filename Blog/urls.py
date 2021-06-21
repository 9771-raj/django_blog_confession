from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
      path("",views.index,name="index"),
      path("blog/",views.blog_corner,name="blog"),
      path("confession/",views.confession_corner,name="confession"),
      path("add_blog/",views.add_blog,name="add_blog"),
      path("add_conf/",views.add_conf,name="add_conf"),
]