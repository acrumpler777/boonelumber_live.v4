from django.contrib import admin
from django.db import models
from .models import *

# Register your models here.
admin.site.register(purchase_order_model)
admin.site.register(product)
admin.site.register(adjustment_model)
admin.site.register(sales_order_model)


