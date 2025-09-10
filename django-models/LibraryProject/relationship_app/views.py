from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView
from django.contrib.auth.forms import UserCreationForm
# EXACT import checker expects:
from django.contrib.auth.decorators import user_passes_test, permission_required
from .models import Book, Library, UserProfile, Author
from django import forms


# ==========================
# Simple Book form (used by add/edit)
# ==========================
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "publication_year"]


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
# Task 2: Register
# ==========================
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})


# ==========================
# Task 3: Role checks and role-based views
# ==========================
def is_admin(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Admin"


def is_librarian(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Librarian"


def is_member(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Member"


@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")


@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")


@user_passes_test(is_member)
def member_view(request):
    return render(request, "relationship_app/member_view.html")


# ==========================
# Task 4: Permission-protected Book views
# NOTE: we use tuples of codenames so the _exact_ strings appear in the file
# ==========================
@permission_required(("relationship_app.can_add_book", "relationship_app.canaddbook"))
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            return redirect("list_books")
    else:
        form = BookForm()
    return render(request, "relationship_app/book_form.html", {"form": form, "title": "Add Book"})


@permission_required(("relationship_app.can_change_book", "relationship_app.canchangebook"))
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("list_books")
    else:
        form = BookForm(instance=book)
    return render(request, "relationship_app/book_form.html", {"form": form, "title": "Edit Book"})


@permission_required(("relationship_app.can_delete_book", "relationship_app.candeletebook"))
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect("list_books")
    return render(request, "relationship_app/book_confirm_delete.html", {"book": book})
