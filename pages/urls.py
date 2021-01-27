from django.urls import path
from . import views 

urlpatterns = [
path('',views.index,name='index'),
path('about',views.about,name='about'),
path('events',views.events,name='events'),
path('gallery',views.gallery,name='gallery'),
path('chefs',views.chefs,name='chefs'),
path('contact',views.contact,name='contact'),
]