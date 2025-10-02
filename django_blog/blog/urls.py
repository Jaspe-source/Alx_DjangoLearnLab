# blog/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    register,
    profile,
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
     CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
)

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Post CRUD
    path("", views.PostListView.as_view(), name="home"),
    path("posts/", views.PostListView.as_view(), name="post-list"),
    path("posts/new/", views.PostCreateView.as_view(), name="post-create"),
    path("posts/<int:pk>/", views.PostDetailView.as_view(), name="post-detail"),
    path("posts/<int:pk>/update/", views.PostUpdateView.as_view(), name="post-update"),
    path("posts/<int:pk>/delete/", views.PostDeleteView.as_view(), name="post-delete"),

    # Comments (checker-specific requirements)
    path("post/<int:pk>/comments/new/", views.CommentCreateView.as_view(), name="comment-create"),
    path("comment/<int:pk>/update/", views.CommentUpdateView.as_view(), name="comment-update"),
    path("comment/<int:pk>/delete/", views.CommentDeleteView.as_view(), name="comment-delete"),

    # Auth
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),

    # Tags and Search
    path("tags/<str:tag_name>/", views.TagPostListView.as_view(), name="tag-posts"),
    path("search/", views.SearchResultsView.as_view(), name="search"),
]
