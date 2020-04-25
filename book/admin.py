from django.contrib import admin
from .models import UserCrudentials,Inventory,Invoice

# Register your models here.
admin.site.register(UserCrudentials)
admin.site.register(Inventory)
