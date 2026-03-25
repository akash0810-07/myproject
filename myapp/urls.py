from django.urls import path

from .views import delete_member, home, update_member


urlpatterns = [
    path("", home, name="home"),
    path("members/<int:member_id>/update/", update_member, name="update_member"),
    path("members/<int:member_id>/delete/", delete_member, name="delete_member"),
]
