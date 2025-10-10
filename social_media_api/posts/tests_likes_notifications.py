from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
from posts.models import Post, Like
from notifications.models import Notification

User = get_user_model()


class LikesNotificationsTests(APITestCase):
    def setUp(self):
        self.u1 = User.objects.create_user(username='u1', password='pw1')
        self.u2 = User.objects.create_user(username='u2', password='pw2')
        self.post = Post.objects.create(author=self.u2, title='Post', content='Content')

    def test_like_generates_notification(self):
        self.client.login(username='u1', password='pw1')
        resp = self.client.post(f'/api/posts/posts/{self.post.id}/like/')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Like.objects.filter(post=self.post, user=self.u1).exists())
        # notification created for post author
        self.assertTrue(Notification.objects.filter(recipient=self.u2, actor=self.u1, verb__icontains='liked').exists())

    def test_unlike(self):
        self.client.login(username='u1', password='pw1')
        self.client.post(f'/api/posts/posts/{self.post.id}/like/')
        resp = self.client.post(f'/api/posts/posts/{self.post.id}/unlike/')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertFalse(Like.objects.filter(post=self.post, user=self.u1).exists())

    def test_notifications_list(self):
        # create a notification manually
        Notification.objects.create(recipient=self.u2, actor=self.u1, verb='liked your post')
        self.client.login(username='u2', password='pw2')
        resp = self.client.get('/api/notifications/')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertTrue(isinstance(resp.data, list) or resp.data)
