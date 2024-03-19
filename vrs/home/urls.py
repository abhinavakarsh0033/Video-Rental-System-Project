from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name="login"),
    path("about",views.about,name='about'),
    path("home",views.home,name='home'),
    path("contact",views.contact,name='contact'),
    path("signup",views.signup,name='signup'),
]