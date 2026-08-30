from django.urls import path

from .views import csrf_token

urlpatterns = [
    path("", csrf_token, name="csrf_token"),
]
