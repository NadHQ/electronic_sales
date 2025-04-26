from drf_yasg import openapi

product_id_param = openapi.Parameter(
    "product_id",
    openapi.IN_QUERY,
    description="Filter by product id",
    type=openapi.TYPE_INTEGER,
)

country_param = openapi.Parameter(
    "country",
    openapi.IN_QUERY,
    description="Filter by country name",
    type=openapi.TYPE_STRING,
)
