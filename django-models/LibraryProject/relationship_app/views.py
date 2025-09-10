from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test
from .models import Book, Library


# ==========================
# Task 1: List Books + Library Detail
# ==========================

def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"


# ==========================
# Task 2: User Registration
# ==========================

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")  # redirect to login after successful registration
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})


# ==========================
# Task 3: Role Checks
# ==========================

def is_admin(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Admin"

def is_librarian(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Librarian"

def is_member(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Member"


# ==========================
# Task 3: Role-Based Views
# ==========================

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")

@user_passes_test(is_member)
def member_view(request):
    return render(request, "relationship_app/member_view.html")
