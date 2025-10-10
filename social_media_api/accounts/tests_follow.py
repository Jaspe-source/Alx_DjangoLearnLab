from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
from posts.models import Post

User = get_user_model()


class FollowFeedTests(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='pass1')
        self.user2 = User.objects.create_user(username='user2', password='pass2')
        self.user3 = User.objects.create_user(username='user3', password='pass3')

        # user2 and user3 create posts
        Post.objects.create(author=self.user2, title='Post by u2', content='content')
        Post.objects.create(author=self.user3, title='Post by u3', content='content')

    def test_follow_and_feed(self):
        # authenticate as user1
        self.client.login(username='user1', password='pass1')

        # follow user2
        resp = self.client.post(f'/api/accounts/follow/{self.user2.id}/')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

        # get feed - should include user2's post but not user3's
        resp = self.client.get('/api/posts/feed/')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        results = resp.data.get('results') or resp.data  # depending on pagination
        # find titles
        titles = [item.get('title') for item in results]
        self.assertIn('Post by u2', titles)
        self.assertNotIn('Post by u3', titles)

        # unfollow user2
        resp = self.client.delete(f'/api/accounts/follow/{self.user2.id}/')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

        # feed should be empty now
        resp = self.client.get('/api/posts/feed/')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        results = resp.data.get('results') or resp.data
        self.assertEqual(len(results), 0)
