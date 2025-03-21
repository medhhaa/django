# to access views from a browser, we use urls.py
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
]
