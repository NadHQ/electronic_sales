from decimal import Decimal

from celery import shared_task

from network.models import NetworkNode
from network.utils.debt import update_debt


@shared_task
def add_debt_task():
    upgraded = update_debt(increase=True, min_value=5, max_value=500)

    print(f"Upgraded {upgraded} nodes")


@shared_task
def reduce_debt_task():
    upgraded = update_debt(increase=False, min_value=100, max_value=10000)

    print(f"Upgraded {upgraded} nodes")


@shared_task
def clear_debt_task(ids):
    updated_count = NetworkNode.objects.filter(id__in=ids).update(debt=Decimal("0.00"))

    return updated_count
