from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Follower
from .serializers import FollowSerializer


class FollowerList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = FollowSerializer
    queryset = Follower.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FollowerDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = FollowSerializer
    queryset = Follower.objects.all()
