from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType

from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission: allow safe methods for anyone, write methods only for owners.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return getattr(obj, "author", None) == request.user


class PostViewSet(viewsets.ModelViewSet):
    """
    CRUD for Posts. Example like/unlike actions are handled by separate views below.
    """
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """
    CRUD for Comments. Creates a notification for the post author when a new comment is created
    (if the notifications app is present).
    """
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        comment = serializer.save(author=self.request.user)

        # Try to create a notification for the post author (if notifications app exists)
        try:
            from notifications.models import Notification
            if comment.post.author != self.request.user:
                Notification.objects.create(
                    recipient=comment.post.author,
                    actor=self.request.user,
                    verb='commented on your post',
                    target_content_type=ContentType.objects.get_for_model(comment.post),
                    target_object_id=comment.post.id
                )
        except Exception:
            # notifications app may not be present during early development/migrations
            pass


class FeedView(generics.ListAPIView):
    """
    GET /api/posts/feed/ -> returns posts authored by users the current user follows,
    ordered newest first. Requires authentication.
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        following_users = user.following.all()
        return Post.objects.filter(author__in=following_users).order_by('-created_at')


class LikePostView(APIView):
    """
    POST   /api/posts/<pk>/like/   -> like a post
    DELETE /api/posts/<pk>/like/   -> unlike a post

    NOTE: This view assumes you will wire the URL to accept pk and map like/unlike to POST/DELETE.
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)

        like, created = Like.objects.get_or_create(post=post, user=request.user)
        if not created:
            return Response({'detail': 'You have already liked this post.'}, status=status.HTTP_400_BAD_REQUEST)

        # create notification for post author (if notifications app exists and actor != recipient)
        if post.author != request.user:
            try:
                from notifications.models import Notification
                Notification.objects.create(
                    recipient=post.author,
                    actor=request.user,
                    verb='liked your post',
                    target_content_type=ContentType.objects.get_for_model(post),
                    target_object_id=post.id
                )
            except Exception:
                # ignore if notifications app is not installed
                pass

        return Response({'detail': 'Post liked.'}, status=status.HTTP_201_CREATED)

    def delete(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        qs = Like.objects.filter(post=post, user=request.user)
        if not qs.exists():
            return Response({'detail': 'You have not liked this post.'}, status=status.HTTP_400_BAD_REQUEST)

        qs.delete()

        # optionally remove related notifications if notifications app exists
        try:
            from notifications.models import Notification
            Notification.objects.filter(
                recipient=post.author,
                actor=request.user,
                verb__icontains='like',
                target_object_id=post.id
            ).delete()
        except Exception:
            pass

        return Response({'detail': 'Post unliked.'}, status=status.HTTP_200_OK)
