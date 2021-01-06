from django.urls import path

from . import views


app_name = 'news'
urlpatterns = [
    path('', views.index, name='index'),
    path('category/', views.category, name='category'),
    path('<int:id>/', views.view, name='info')
]