from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)
    country = models.CharField(max_length=100)
    phone = models.CharField(max_length=16)
    email = models.EmailField(max_length=50)
    website = models.CharField(max_length=50)
    nip = models.CharField(max_length=12)
    def __str__(self):
        return self.name
