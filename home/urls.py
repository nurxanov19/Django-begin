from django.urls import path
from .views import about_page, home_page, contact_page, project_page

urlpatterns = [
    path('', home_page),
    path('about/', about_page),
    path('contact/', contact_page),
    path('project/', project_page),
]