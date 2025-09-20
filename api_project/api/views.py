# api/views.py
from rest_framework import generics, viewsets
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Book
from .serializers import BookSerializer

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission: read allowed for any request;
    write allowed only to owner or staff.
    """
    def has_object_permission(self, request, view, obj):
        # read-only
        if request.method in permissions.SAFE_METHODS:
            return True
        # write permissions only for owner or staff
        return obj.owner == request.user or request.user.is_staff

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('-id')
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        # set owner automatically
        serializer.save(owner=self.request.user)
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # New CRUD ViewSet
class BookViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard CRUD actions
    (list, create, retrieve, update, destroy) for the Book model.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
