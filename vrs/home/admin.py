from django.contrib import admin
from home.models import UserProfile
from home.models import Movie


# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Movie)