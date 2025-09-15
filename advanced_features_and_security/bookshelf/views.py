from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from django.http import HttpResponse


@permission_required('bookshelf.can_view', raise_exception=True)
def view_books(request):
    return HttpResponse("You have permission to VIEW books.")


@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    return HttpResponse("You have permission to CREATE books.")


@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request):
    return HttpResponse("You have permission to EDIT books.")


@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request):
    return HttpResponse("You have permission to DELETE books.")
