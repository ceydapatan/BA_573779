from django.urls import path
from . import views

urlpatterns = [
    path('', views.period_list, name='period_list'),
    path('period/new', views.period_new, name='period_new'),
]
