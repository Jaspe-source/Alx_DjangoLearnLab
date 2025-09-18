from django.urls import path
from . import views

urlpatterns = [
    path('form-example/', views.form_example_view, name='form_example'),
]
