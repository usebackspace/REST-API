from django.urls import path
from . import views

urlpatterns = [
    path('hero/<int:pk>',views.hero),
    path('hero_all/',views.hero_all)
]


