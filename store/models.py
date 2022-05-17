
from django.db import models

# Create your models here.
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Store(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    img_url = models.URLField()
    category = models.ManyToManyField(Category)
    distance = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("store", args=[str(self.id)])

    def get_simple_address(self):
        return self.address.split(' ')[-1]
