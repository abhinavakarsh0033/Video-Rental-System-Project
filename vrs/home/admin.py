from django.contrib import admin
from home.models import UserProfile
from home.models import Movie
from home.models import Cart_Item
from home.models import Order
from home.models import Invoice


# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    readonly_fields = ('user','phone','dob','gender')
admin.site.register(UserProfile,UserProfileAdmin)

admin.site.register(Movie)

class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('due_date','user','movie','total_price','isrented','invoice_id','order_date')
admin.site.register(Order,OrderAdmin)

class InvoiceAdmin(admin.ModelAdmin):
    readonly_fields = ('invoice_id','invoice_date','total_price','order')
admin.site.register(Invoice,InvoiceAdmin)