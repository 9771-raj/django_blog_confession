from django.contrib import admin

# Register your models here.
from .models import contact,confession,blog
admin.site.register(contact)
admin.site.register(confession)
admin.site.register(blog)
