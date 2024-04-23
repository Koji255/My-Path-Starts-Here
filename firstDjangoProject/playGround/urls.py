from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.sayHello),
    path('hello2user/', views.sayHelloToUser),
]