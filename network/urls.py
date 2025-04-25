from rest_framework.routers import DefaultRouter

from network.views import NetworkNodeViewSet

router = DefaultRouter()
router.register(prefix=r"nodes", viewset=NetworkNodeViewSet)

urlpatterns = router.urls
