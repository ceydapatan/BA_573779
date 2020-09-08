from django.conf.urls import url
from django.urls import include, path

from . import views

app_name = 'cal'
urlpatterns = [
    url('', views.CalendarView.as_view(), name='calendar'),

]