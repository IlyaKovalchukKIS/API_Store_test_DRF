from django.urls import path
from rest_framework.routers import DefaultRouter

from store.apps import StoreConfig
from store.views import AdvertisementViewSet, UserViewSet, UserViewCreate

app_name = StoreConfig.name

router = DefaultRouter()
router.register(
    r"store",
    AdvertisementViewSet,
    basename="store",
)
router.register(
    r"users",
    UserViewSet,
    basename="users",
)
urlpatterns = []
urlpatterns += router.urls
urlpatterns += [path("create/", UserViewCreate.as_view())]
