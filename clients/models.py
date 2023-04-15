from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=150)
    type = models.CharField(max_length=150)
    partner = models.CharField(max_length=150)
    contact = models.CharField(max_length=150)
    phone_number_simple = models.CharField(max_length=150)
    phone_number_work = models.CharField(max_length=150)
    email = models.EmailField()
    city = models.CharField(max_length=150)
    country = models.CharField(max_length=150)
    sector = models.CharField(max_length=150)
    serial_number = models.CharField(max_length=150)
    inv_number = models.CharField(max_length=150)
