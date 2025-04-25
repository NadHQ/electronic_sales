import random
from decimal import Decimal

from network.models import NetworkNode


def update_debt(increase: bool, min_value: int, max_value: int) -> int:
    queryset = NetworkNode.objects.all()
    upgraded_nodes = []

    for node in queryset:
        amount = Decimal(random.uniform(min_value, max_value)).quantize(Decimal("0.01"))
        if increase:
            node.debt += amount
        else:
            node.debt = max(Decimal("0.00"), node.debt - amount)
        upgraded_nodes.append(node)

    NetworkNode.objects.bulk_update(upgraded_nodes, ["debt"])

    return len(upgraded_nodes)
