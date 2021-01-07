from django.contrib import admin
from .models import Profile, CourseEnrolled, LabEnrolled

admin.site.register(Profile)
admin.site.register(CourseEnrolled)
admin.site.register(LabEnrolled)

# Register your models here.
