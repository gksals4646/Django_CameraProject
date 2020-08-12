from django.contrib import admin
<<<<<<< HEAD
from .models import Product, BodyType, LensType, Brand

# Register your models here.
admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(BodyType)
admin.site.register(LensType)
=======
from .models import *
# Register your models here.
admin.site.register(LensType)
admin.site.register(BodyType)
admin.site.register(Brand)
admin.site.register(Product)
>>>>>>> 0811석근시작1
