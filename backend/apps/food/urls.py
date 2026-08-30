from django.urls import path

from . import views

urlpatterns = [
    path("create", views.create_food_view, name="Create Food"),
    path("all", views.all_view, name="List all Foods"),
]
