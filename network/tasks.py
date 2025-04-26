from decimal import Decimal

from celery import shared_task
from django.core.mail import EmailMessage

from electronic_sales.settings import DEFAULT_FROM_EMAIL
from network.models import NetworkNode
from network.utils.debt import update_debt
from network.utils.qr_code_builder import QrCodeBuilder


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


@shared_task
def send_qr_code_email(target_node_id, target_email):
    node = NetworkNode.objects.select_related("address").get(id=target_node_id)

    data = {
        "email": node.email,
        "country": node.address.country if node.address else "",
        "city": node.address.city if node.address else "",
        "street": node.address.street if node.address else "",
        "building_number": node.address.building_number if node.address else "",
    }

    qr_code_builder = QrCodeBuilder(data=data)
    qr_code = qr_code_builder.build_contacts_qr_code(data=data)

    email = EmailMessage(
        subject="Ваш QR-код с контактами",
        body="Здравствуйте! Во вложении QR-код с контактной информацией.",
        from_email=DEFAULT_FROM_EMAIL,
        to=[target_email],
    )
    email.attach("contact_qrcode.png", qr_code.read(), "image/png")
    email.send()
