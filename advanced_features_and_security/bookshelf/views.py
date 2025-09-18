from django.shortcuts import render
from .forms import ExampleForm

def form_example_view(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Securely handle cleaned data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            return render(request, 'bookshelf/form_example.html', {
                'form': ExampleForm(),
                'success': f"Form submitted successfully! Name: {name}, Email: {email}"
            })
    else:
        form = ExampleForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})
