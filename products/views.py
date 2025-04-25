# Create your views here.


from rest_framework import viewsets

from products.models import Product
from products.serializers import ProductSerializer
from users.permisions import IsActiveUserPermission


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsActiveUserPermission]
