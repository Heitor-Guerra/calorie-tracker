from django.urls import path

from . import views

urlpatterns = [
    path("create", views.create_user_view, name="Create User"),
    path("login", views.login_view, name="Login"),
    path("logout", views.logout_view, name="Logout"),
    path("logged-user", views.get_logged_user_view, name="Get Logged User"),
    # Not Used
    path("change-password", views.change_password_view, name="Change User Password"),
    path("edit", views.edit_user_view, name="Edit User"),
    path("edit/<int:user_id>", views.edit_user_admin_view, name="Edit User"),
    path("delete", views.delete_view, name="Delete User"),
    path("all", views.all_view, name="List all Users"),
]
