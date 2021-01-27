from django.urls import path
from . import views

urlpatterns = [
path('',views.menu,name='menu'),
path('specials',views.specials,name='specials'),
path('book',views.book,name='book'),
]