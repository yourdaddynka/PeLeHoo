from django.urls import path

from . import views

urlpatterns = [
    path("", views.library_view, name="index"),
]