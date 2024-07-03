# start_django/app/urls.py

from django.urls import path
from app import views

urlpatterns = [
    path("top/", views.top, name="top")
]