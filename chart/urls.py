from django.urls import path
from . import views

app_name = "chart"

urlpatterns = [
    path('', views.home, name="home")
    
]
