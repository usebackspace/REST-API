from django.urls import path
from . import views


urlpatterns = [
    path('heroapi/',views.hero_api)
]
