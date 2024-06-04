from django.contrib import admin
from products.models import Product
from products.models import Customer


admin.site.register(Product)
admin.site.register(Customer)
admin.site.site_header = "E-commerce Admin: testing Django for the first time"
