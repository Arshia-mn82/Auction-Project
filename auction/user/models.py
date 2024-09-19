from django.db import models
from django.contrib.auth.models import User


class Auctions(models.Model):
    name = models.CharField(max_length=100)


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    auctions = models.ManyToManyField(Auctions)


class Provider(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    auctions = models.ManyToManyField(Auctions)


class Product(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    base_price = models.FloatField()
    highest_price = models.FloatField(default=base_price)
    auctions = models.ForeignKey(Auctions, on_delete=models.CASCADE)


class Offer(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    price = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
