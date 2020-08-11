from django.contrib import admin
from .models import Product, BodyType, LensType, Brand

# Register your models here.
admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(BodyType)
admin.site.register(LensType)