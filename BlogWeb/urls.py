
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from users import views as users_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("Blog.urls")),
    path('register/',users_view.register,name="register"),
    path('profile/',users_view.profile,name="profile"),
    path('edit/<int:id>',users_view.edit,name="edit"),
    path('edit_confession/<int:id>',users_view.edit_confession,name="edit_confession"),
    path('delete/<int:id>',users_view.delete,name="delete"),
    path('delete_conf/<int:id>',users_view.delete_conf,name="delete_conf"),
    path('login/',auth_views.LoginView.as_view(template_name="users/login.html"),name="login"),
    path('logout/',auth_views.LogoutView.as_view(template_name="users/logout.html"),name="logout"),
]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
