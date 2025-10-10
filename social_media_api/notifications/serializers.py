from rest_framework import serializers
from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    actor_username = serializers.ReadOnlyField(source='actor.username')

    class Meta:
        model = Notification
        fields = ['id', 'recipient', 'actor', 'actor_username', 'verb', 'target', 'unread', 'timestamp']
        read_only_fields = ['recipient', 'actor', 'target', 'timestamp']
