from django.urls import path

from . import views

urlpatterns = [
    path("", views.DailyLogCRUDView.as_view(), name="CRUD Operations on DailyLog"),
]
