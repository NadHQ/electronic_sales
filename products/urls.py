from rest_framework.routers import DefaultRouter

from products.views import ProductViewSet

router = DefaultRouter()
router.register(prefix=r"products", viewset=ProductViewSet)

urlpatterns = router.urls
