from django.urls import path
from . import views

urlpatterns = [
    path("view/", views.view_books, name="view_books"),
    path("create/", views.create_book, name="create_book"),
    path("edit/", views.edit_book, name="edit_book"),
    path("delete/", views.delete_book, name="delete_book"),
]
