from django.urls import path
from .views import describe_options, pro, plus

urlpatterns = [
    path('describe/', describe_options),
    path('pro/', pro),
    path('plus/', plus)
]