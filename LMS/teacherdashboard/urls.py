from django.urls import path
from . import views

urlpatterns = [
    path('tdashboard', views.Teacherdashboard.as_view(), name="teacherdashboard"),
]