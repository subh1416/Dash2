from django.urls import path
#now import the views.py file into this code
from . import views
urlpatterns=[
  path('old', views.main_view, name='main_view'),
  path('',views.home, name="home"),
  path('home',views.home, name="home"),
  path('satellite',views.satellite, name="satellite"),
  path('packet',views.packet, name="packet"),
  path('station',views.station, name="station"),
  
 
]