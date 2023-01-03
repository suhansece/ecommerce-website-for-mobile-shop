from django.contrib import admin

from .models import Product,Brand,Customer,Order,OrderItem,ShippingAddress


admin.site.register(Brand)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)


