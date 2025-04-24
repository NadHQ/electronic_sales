from django.contrib import admin


@admin.action(description="Очистить задолженность перед поставщиком")
def clear_debt(modeladmin, request, queryset):
    """
    Admin action for clearing debt
    """
    queryset.update(debt=0)
