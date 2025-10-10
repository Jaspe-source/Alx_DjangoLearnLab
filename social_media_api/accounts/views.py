from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from django.contrib.auth import login

from .serializers import RegisterSerializer, LoginSerializer, UserProfileSerializer

User = get_user_model()


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = User.objects.get(username=response.data['username'])
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user': response.data}, status=status.HTTP_201_CREATED)


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        login(request, user)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user': UserProfileSerializer(user).data}, status=status.HTTP_200_OK)


class UserProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserProfileSerializer

    def get_object(self):
        return self.request.user


class FollowToggleView(APIView):
    """
    POST /api/accounts/follow/<int:user_id>/  -> follow user_id
    DELETE /api/accounts/follow/<int:user_id>/ -> unfollow user_id
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        target = get_object_or_404(User, id=user_id)
        if target == request.user:
            return Response({'detail': "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        # Add to following of current user and add to followers of target
        request.user.following.add(target)
        # Keep followers field consistent as well
        target.followers.add(request.user)

        return Response({'detail': f'You are now following {target.username}.'}, status=status.HTTP_200_OK)

    def delete(self, request, user_id):
        target = get_object_or_404(User, id=user_id)
        if target == request.user:
            return Response({'detail': "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        request.user.following.remove(target)
        target.followers.remove(request.user)

        return Response({'detail': f'You have unfollowed {target.username}.'}, status=status.HTTP_200_OK)


class FollowersListView(generics.ListAPIView):
    """
    GET /api/accounts/<int:user_id>/followers/ -> list followers of user_id
    """
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        user = get_object_or_404(User, id=user_id)
        # Return queryset of users who follow this user
        return user.followers.all()


class FollowingListView(generics.ListAPIView):
    """
    GET /api/accounts/<int:user_id>/following/ -> list users that user_id is following
    """
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        user = get_object_or_404(User, id=user_id)
        return user.following.all()
