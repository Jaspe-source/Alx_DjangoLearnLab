from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, "book_list.html", {"books": books})

@permission_required("bookshelf.can_view_restricted", raise_exception=True)
def restricted_view(request):
    return HttpResponse("This is a restricted section, only visible to users with the right permission.")

