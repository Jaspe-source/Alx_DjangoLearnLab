from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
from .models import Book, Library

# Task 1 - keep this so LOGIN_REDIRECT_URL works
@login_required
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Task 2 - User Registration
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # log the user in after registration
            return redirect('list_books')  # redirect to books page after signup
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Task 1 - Class-based view (still needed for checker consistency)
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
