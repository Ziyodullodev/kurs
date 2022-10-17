from django.urls import path
from .views import home, bot

urlpatterns = [
    path('', home, name="home"),
    path('bot/', bot, name="bot"),
]