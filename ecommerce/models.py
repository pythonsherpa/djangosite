from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(unique=True)
    notes = models.CharField(max_length=255, blank=True, null=True)


class Product:
    # TODO: create a product model (and inherit from models.Model)
    ...
