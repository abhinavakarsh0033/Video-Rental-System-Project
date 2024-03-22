from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name="login"),
    path("about",views.about,name='about'),
    path("home",views.home,name='home'),
    path("contact",views.contact,name='contact'),
    path("signup",views.signup,name='signup'),
    path("signout",views.signout,name='signout'),
    path("action",views.action,name='action'),
    path("comedy",views.comedy,name='comedy'),
    path("drama",views.drama,name='drama'),
    path("horror",views.horror,name='horror'),
    path("romance",views.romance,name='romance'),
    path("thriller",views.thriller,name='thriller'),
    path("search",views.search,name='search'),
    path("movie/<int:id>",views.movie,name='movie'),
    path("add_to_cart/<int:id>",views.add_to_cart,name='add_to_cart'),

]