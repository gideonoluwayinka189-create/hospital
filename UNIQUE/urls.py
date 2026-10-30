
from django.urls import path
from UNIQUE import views

urlpatterns = [
    path('', views.index, name='index'),
]