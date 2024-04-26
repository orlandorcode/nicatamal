from django.contrib import admin

# Register your models here.

from order_app.models import Client,Product,ClientType,Order,UserProfileInfo

admin.site.register(Client)
admin.site.register(Product)
admin.site.register(ClientType)
admin.site.register(Order)
admin.site.register(UserProfileInfo)

