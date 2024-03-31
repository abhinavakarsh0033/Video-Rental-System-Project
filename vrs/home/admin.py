from django.contrib import admin
from home.models import UserProfile
from home.models import Movie
from home.models import Cart_Item
from home.models import Order
from home.models import Invoice


# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Movie)
admin.site.register(Cart_Item)
# admin.site.register(Order)

class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('order_id','order_date')

admin.site.register(Order,OrderAdmin)
admin.site.register(Invoice)