from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, mixins, generics

from store.models import Advertisement
from store.serializers import AdvertisementSerializer, UserSerializer


class AdvertisementViewSet(viewsets.ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserViewCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
