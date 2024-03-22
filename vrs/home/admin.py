from django.contrib import admin
from home.models import UserProfile
from home.models import Movie
from home.models import Cart_Item


# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Movie)
admin.site.register(Cart_Item)