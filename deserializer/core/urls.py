from django.urls import path
from . import views
urlpatterns = [
    path('marvel/',views.marvel),
   
]
