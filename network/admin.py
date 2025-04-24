from django.contrib import admin

from network.actions import clear_debt
from network.models import Address, NetworkNode

# Register your models here.

# admin.site.register(NetworkNode)
admin.site.register(Address)


@admin.register(NetworkNode)
class NetworkNodeAdmin(admin.ModelAdmin):
    """
    NetworkNode admin class
    """

    list_display = [
        "name",
        "node_type",
        "email",
        "employees_number",
        "debt",
        "created_at",
        "get_city",
    ]
    list_filter = ["node_type", "address__city"]
    search_fields = ["name", "email", "address__city"]

    actions = [clear_debt]

    def get_city(self, obj):
        """
        Get city of node
        """
        return obj.address.city
