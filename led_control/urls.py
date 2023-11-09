from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Alphabet/', views.index,  name = 'Alphabet'),
    path('led_control/', views.control_led,  name = 'led_control'),
]
