from drf_yasg import openapi

filter_by_product_id = openapi.Parameter(
    "product_id",
    openapi.IN_QUERY,
    description="Filter by this product id",
    type=openapi.TYPE_INTEGER,
)

filter_by_country_name = openapi.Parameter(
    "country",
    openapi.IN_QUERY,
    description="Filter by this country name",
    type=openapi.TYPE_STRING,
)
