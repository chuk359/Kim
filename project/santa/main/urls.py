from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('takepart', views.takepart, name='takepart' ),
    path('present', views.present, name='present' )
  ]
