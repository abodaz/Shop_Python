from django.db import models


class Prodcuts(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    stock = models.IntegerField()
    image = models.CharField(max_length=2083)


class Offer(models.Model):
    code = models.CharField(max_length=10)
    discount = models.FloatField()
    description = models.CharField(max_length=255)






