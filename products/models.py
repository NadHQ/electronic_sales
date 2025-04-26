from django.db import models

# Create your models here.


class Product(models.Model):
    """
    Model describing product entity
    """

    name = models.CharField(max_length=50)
    model = models.CharField(max_length=255)
    release_date = models.DateField()
    distributed_by = models.ManyToManyField(
        "network.NetworkNode", related_name="products"
    )
