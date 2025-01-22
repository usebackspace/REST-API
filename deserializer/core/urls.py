from django.urls import path
from . import views
urlpatterns = [
    path('newmarvel/',views.new_marvel),
]
