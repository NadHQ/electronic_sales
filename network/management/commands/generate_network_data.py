import random
from datetime import timedelta

from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker

from network.models import Address, NetworkNode
from products.models import Product


class Command(BaseCommand):
    help = "Generate fake data for Address, NetworkNode, and Product models"

    def handle(self, *args, **options):
        fake = Faker()

        # Creating Addresses
        addresses = []
        for _ in range(50):
            address = Address.objects.create(
                country=fake.country(),
                city=fake.city(),
                street=fake.street_name(),
                building_number=fake.building_number(),
            )
            addresses.append(address)

        # Create Nodes
        nodes = []

        factories = []
        for _ in range(5):
            node = NetworkNode.objects.create(
                name=fake.company(),
                node_type="factory",
                email=fake.company_email(),
                address=addresses.pop(),
                employees_number=random.randint(50, 500),
                debt=round(random.uniform(0, 10000), 2),
            )
            nodes.append(node)
            factories.append(node)

        distributors = []
        for _ in range(10):
            node = NetworkNode.objects.create(
                name=fake.company(),
                node_type="distributor",
                email=fake.company_email(),
                address=addresses.pop(),
                employees_number=random.randint(20, 200),
                supplier=random.choice(factories),
                debt=round(random.uniform(0, 5000), 2),
            )
            nodes.append(node)
            distributors.append(node)

        for _ in range(20):
            node = NetworkNode.objects.create(
                name=fake.company(),
                node_type=random.choice(["dealer", "retail"]),
                email=fake.company_email(),
                address=addresses.pop(),
                employees_number=random.randint(5, 50),
                supplier=random.choice(distributors),
                debt=round(random.uniform(0, 2000), 2),
            )
            nodes.append(node)

        dealers_and_retails = [n for n in nodes if n.node_type in ["dealer", "retail"]]
        for _ in range(15):
            node = NetworkNode.objects.create(
                name=fake.company(),
                node_type="individual",
                email=fake.email(),
                address=addresses.pop(),
                employees_number=random.randint(1, 10),
                supplier=random.choice(dealers_and_retails),
                debt=round(random.uniform(0, 500), 2),
            )
            nodes.append(node)

        # Create products
        for _ in range(30):
            product = Product.objects.create(
                name=fake.word().capitalize(),
                model=fake.lexify(text="Model ???"),
                release_date=timezone.now().date()
                - timedelta(days=random.randint(30, 1000)),
            )
            product.distributed_by.set(random.sample(nodes, random.randint(1, 5)))

        self.stdout.write(self.style.SUCCESS("✅ Данные успешно сгенерированы!"))
