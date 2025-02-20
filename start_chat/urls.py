from django.urls import path
from .views import start, history

urlpatterns = [
    path('start/', start),
    path('history/', history)
]