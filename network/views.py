# Create your views here.

from typing import List

from django.db.models import Avg
from django.http import HttpRequest
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from network.models import NetworkNode
from network.serializers import NetworkNodeDetailSerializer, NetworkNodeSerializer
from network.swagger.parameters import filter_by_country_name, filter_by_product_id
from users.permisions import IsActiveUserPermission


class NetworkNodeViewSet(viewsets.ModelViewSet):
    queryset = NetworkNode.objects.all()
    serializer_class = NetworkNodeSerializer
    permission_classes = [IsActiveUserPermission]

    def get_queryset(self):
        queryset: List[NetworkNode] = super().get_queryset()
        country = self.request.query_params.get("country")

        if country:
            queryset = queryset.filter(address__country__iexact=country)

        return queryset

    @swagger_auto_schema(
        manual_parameters=[filter_by_country_name],
        operation_description="Get list of nodes filtered by country name",
        responses={200: NetworkNodeDetailSerializer(many=True)},
    )
    @action(
        methods=["get"],
        detail=False,
        serializer_class=NetworkNodeDetailSerializer,
    )
    def filtered_list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Get all nodes above average debt",
        responses={200: NetworkNodeDetailSerializer(many=True)},
    )
    @action(
        methods=["get"],
        detail=False,
        serializer_class=NetworkNodeDetailSerializer,
    )
    def above_avarage_debt(self, request):
        avg_debt = NetworkNode.objects.aggregate(avg=Avg("debt"))["avg"]
        nodes = NetworkNode.objects.filter(debt__gt=avg_debt)
        serializers = self.get_serializer(nodes, many=True)
        return Response(serializers.data)

    @swagger_auto_schema(
        manual_parameters=[filter_by_product_id],
        operation_description="Filter by product id",
        responses={200: NetworkNodeDetailSerializer(many=True)},
    )
    @action(
        methods=["get"],
        detail=False,
        serializer_class=NetworkNodeDetailSerializer,
    )
    def filter_by_product_id(self, request: HttpRequest):
        product_id = request.query_params.get("product")
        if not product_id:
            return Response(
                {"error": "product_id is required"}, status=status.HTTP_400_BAD_REQUEST
            )

        nodes = NetworkNode.objects.filter(products__id=product_id)
        serializers = self.get_serializer(nodes, many=True)
        return Response(serializers.data)
