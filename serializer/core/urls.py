from django.urls import path
from . import views
urlpatterns = [
    path('',views.marvel),
    path('marvel/<int:id>',views.marvel_id),
    path('marvel/',views.marvel_all)
]
