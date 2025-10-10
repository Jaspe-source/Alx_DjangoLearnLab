from django.urls import path
from .views import NotificationsListView, MarkNotificationReadView

urlpatterns = [
    path('', NotificationsListView.as_view(), name='notifications-list'),
    path('<int:pk>/read/', MarkNotificationReadView.as_view(), name='notification-mark-read'),
]
