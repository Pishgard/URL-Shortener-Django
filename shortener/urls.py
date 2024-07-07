from django.urls import path
from .views import index, list, url_redirect

app_name = 'shortener'

urlpatterns = [
    path('', index, name='index'),
    path('list/', list, name='list'),
    path('<str:slug>/', url_redirect, name="redirect")
]