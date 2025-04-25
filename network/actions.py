from decimal import Decimal

from django.contrib import admin, messages
from django.db.models import QuerySet

from network.tasks import clear_debt_task


@admin.action(description="Очистить задолженность перед поставщиком")
def clear_debt(modeladmin: admin.ModelAdmin, request, queryset: QuerySet):
    """
    Admin action for clearing debt
    """

    count = queryset.count()
    if count > 20:
        ids = list(queryset.values_list("id", flat=True))
        clear_debt_task.delay(ids)
        modeladmin.message_user(
            request,
            f"Задача на очистку задолженности запущена для {count} объектов. Это займет немного времени",
            messages.INFO,
        )
    else:
        updated = queryset.update(debt=Decimal("0.00"))
        modeladmin.message_user(
            request,
            f"Задолженность очищена у {updated} объектов",
            message=messages.SUCCESS,
        )
