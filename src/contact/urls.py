
from django.urls import path

from . import views
app_name = 'news'
urlpatterns = [
    path('', views.contact, name='index'),
    path('contact/', views.next, name = 'form'),

]