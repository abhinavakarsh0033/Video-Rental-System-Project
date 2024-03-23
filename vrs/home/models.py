from typing import Any
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from datetime import timedelta
from django.db.models.fields import DurationField
#importing pillow
from PIL import Image

 
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)


    def __str__(self):
        return str(self.user)

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)
    staff_id = models.AutoField(primary_key=True)

    class Meta:
        permissions = [
            ('can_view_orders','Can view orders'),
            ('can_view_users','Can view users'),
            ('can_view_userprofile','Can view user profile'),
            ('can_view_movies','Can view movies'),
            ('can_edit_moviequantity','Can edit movie quantity'),
        ]
    
    
class Movie(models.Model):
    movie_id = models.AutoField(primary_key=True)
    movie_title = models.CharField(max_length=100)
    movie_desc = models.CharField(max_length=1000)
    movie_img = models.ImageField(upload_to='movies/thumbnails')
    # movie_video = models.FileField(upload_to='movies/videos')
    movie_release_year = models.DateField()
    movie_cast = models.CharField(max_length=500)
    movie_genre = models.CharField(max_length=100,choices=[('Action','Action'),('Comedy','Comedy'),('Drama','Drama'),('Horror','Horror'),('Romance','Romance'),('Thriller','Thriller')])
    movie_rent_price = models.IntegerField()
    movie_buy_price = models.IntegerField()
    movie_rent_duration = models.IntegerField()
    movie_runtime  =models.DurationField(_("Duration"), default=timedelta(0), help_text=_("Duration of the movie in minutes"))
    movie_quantity = models.IntegerField(default=10)

    def __str__(self):
        return self.movie_title

class Cart_Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    isrented = models.BooleanField(default=True)
    def __str__(self):
        return str(self.user) + ' ' + str(self.movie)    

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Cart_Item)
    total_price = models.IntegerField()
    order_date = models.DateTimeField(auto_now_add=True)
    order_id = models.AutoField(primary_key=True)

    def __str__(self):
        return str(self.user) + ' ' + str(self.order_date)