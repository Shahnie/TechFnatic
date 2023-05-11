from django.urls import path
from .import views

urlpatterns = [
    path("",views.homePage,name="index"),
    path("contact/",views.Contacts,name="contact"),

]