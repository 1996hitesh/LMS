from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "Dashboard" ),
    path('course/', views.allcourse, name = "Course" ),
    path('course/<int:id>', views.course, name = "Course" ),
    path('course/<int:id>/<int:tid>', views.watch, name = "Watch" )
]