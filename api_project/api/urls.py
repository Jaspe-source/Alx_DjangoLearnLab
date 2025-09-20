# api/urls.py
from rest_framework import routers
from .views import BookViewSet
from django.urls import path
from .views import BookList

router = routers.DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]
