from django.db import models
import datetime
# Create your models here.
class Inventory(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=20)
    ISBN = models.IntegerField()
    price = models.DecimalField(max_digits=6,decimal_places=2)
    img = models.ImageField()
    def __str__(self):
        return self.title

#models for user crudentials
class UserCrudentials(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=128) #hashed password stored
    address = models.CharField(max_length=50)
    zip = models.CharField(max_length=5)
    company = models.CharField(max_length=20)
    salt = models.CharField(max_length=32) # salt string stored for authenticating hashed psw
    date_joined = models.DateField(default=datetime.date.today())

    def __str__(self):
        return self.username

#models for invoice of user's purchases
class Invoice(models.Model):
    invoice_num = models.IntegerField()
    date = models.DateField()
    username = models.CharField(max_length=30)
    address = models.CharField(max_length=20)
    subtotal = models.DecimalField(max_digits=6,decimal_places=2)
    quantity = models.IntegerField()

    def __str__(self):
        return self.invoice_num
