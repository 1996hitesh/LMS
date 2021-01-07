from django.urls import path
from . import views

urlpatterns = [
    path('', views.RdpDownloadView.as_view(), name = "Labs" ),
]