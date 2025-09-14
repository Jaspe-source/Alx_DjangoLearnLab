from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import get_user_model
from .models import Book

User = get_user_model()

@login_required
def book_list(request):
    books = Book.objects.all()
    return render(request, "relationship_app/book_list.html", {"books": books})

@login_required
@permission_required("relationship_app.can_add_book", raise_exception=True)
def restricted_view(request):
    return render(request, "relationship_app/restricted.html")
