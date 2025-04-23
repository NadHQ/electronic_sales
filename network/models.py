from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone
# Create your models here.

class Address(models.Model):
    """
    Model describing address entity of node
    """
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=256)
    building_number = models.CharField(max_length=50)

class NetworkNode(models.Model):
    """
    Model describing node entity in network
    """

    NODE_TYPE_CHOICES = [
        ('factory', 'Завод'),
        ('distributor', 'Дистрибьютор'),
        ('dealer', 'Дилерский центр'),
        ('retail', 'Крупная розничная сеть'),
        ('individual', 'Индивидуальный предприниматель'),
    ]

    name = models.CharField(max_length=50)
    node_type = models.CharField(max_length=25, choices=NODE_TYPE_CHOICES)
    email = models.EmailField()
    address = models.OneToOneField(Address, on_delete=models.CASCADE, related_name="node")
    employees_number = models.IntegerField(default=1, validators=[MinValueValidator(1)])
    supplier = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
    debt = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    created_at = models.DateTimeField(default=timezone.now)
