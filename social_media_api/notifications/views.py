from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Notification
from .serializers import NotificationSerializer

class NotificationsListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # return notifications for current user (unread first)
        return Notification.objects.filter(recipient=self.request.user).order_by('-unread', '-timestamp')


class MarkNotificationReadView(generics.UpdateAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Notification.objects.all()

    def patch(self, request, *args, **kwargs):
        notification = self.get_object()
        if notification.recipient != request.user:
            return Response({'detail': 'Not allowed'}, status=status.HTTP_403_FORBIDDEN)
        notification.unread = False
        notification.save()
        return Response({'detail': 'Marked as read'}, status=status.HTTP_200_OK)
