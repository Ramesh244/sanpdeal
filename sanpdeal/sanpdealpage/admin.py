# from django.contrib import admin

# # from .forms import Detailsaboutpage

# from . models import *

from django.contrib import admin
from sanpdealpage.models import *
from django.contrib import admin
from sanpdealpage.models import *

admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Contact)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAdd)
admin.site.register(DetailsForm)
# from django.contrib import admin
# from .models import *
# from django.admin_site import custom_admin_site
#
# @admin.register(Product, Customer, Order,OrderItem,Contact,DetailsForm,ShippingAdd,site=custom_admin_site)
# class PersonAdmin(admin.ModelAdmin):
#     pass


# class CustumerAdmin(admin.ModelAdmin):
#     pass
# @admin.site.register(Customer,CustumerAdmin)



# class productAdmin(admin.ModelAdmin):
#     pass
# @admin.site.register(Product,productAdmin)

# class orderAdmin(admin.ModelAdmin):
#     pass
# @admin.site.register(Order,orderAdmin)
#
#
# class orderitemAdmin(admin.ModelAdmin):
#     pass
#
# @admin.site.register(OrderItem, orderitemAdmin)
#
#
# class shippingAdmin(admin.ModelAdmin):
#     pass
#
# @admin.site.register(ShippingAdd, shippingAdmin)
#
#
#
#
#
#
# class DetailsFormAdmin(admin.ModelAdmin):
#    pass
#
# @admin.site.register(DetailsForm, DetailsFormAdmin)
#
# class AboutAdmin(admin.ModelAdmin):
#     pass
# @admin.site.register(Contact, AboutAdmin)
#
# class RatingAdmin(admin.ModelAdmin):
#     pass
# @admin.site.register(Rating, RatingAdmin)