from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)  # Django will create a VARCHAR(100) column
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Django will create a DECIMAL(10, 2) column
    amount = models.IntegerField(default=0)  # Django will create an INT column
    description = models.TextField()  # Django will create a TEXT column
    created_at = models.DateTimeField(auto_now_add=True)  # Django will create a DATETIME column that will be updated only when the row is created
    updated_at = models.DateTimeField(auto_now=True)  # Django will create a DATETIME column that will be updated every time the row is updated
    image = models.ImageField(
        upload_to="media/products", null=True, blank=True
        # upload_to is the path where the image will be saved;
        # null=True allows the field to be empty;
        # blank=True allows the field to be empty in the admin panel
    )
    def __str__(self):
        return self.name

#  Exercise TEST
# Create a model called Customer with the following fields:
# name: text, max length of 50
# address: text, max length of 200
# phone: text, max length of 20

class Customer(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    def __str__(self):
        return self.name
