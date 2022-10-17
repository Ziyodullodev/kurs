from django.urls import path
from .views import home, Botpost

urlpatterns = [
    path('', home, name="home"),
    path('bot/', Botpost.as_view(), name="bot"),
]