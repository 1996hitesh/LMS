from django.contrib import admin
from .models import Courses, Modules, Topics

# Register your models here.

admin.site.register(Courses)
admin.site.register(Modules)
admin.site.register(Topics)
