from django.urls import path
from . import views
urlpatterns = [
    path('about/', views.about , name='about' ),
    path('contactus/', views.contactus , name='contactus' ),
    path('contactus/service/', views.servicecontact , name='servicecontact' ),
    path('subscribe/', views.subscribe , name='subscribe' ),
]
