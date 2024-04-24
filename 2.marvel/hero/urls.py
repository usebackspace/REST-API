from django.urls import path
from . import views

urlpatterns = [
    path('hero_create/',views.hero_create)
]

