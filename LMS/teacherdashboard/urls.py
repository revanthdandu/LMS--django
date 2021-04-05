from django.urls import path
from . import views

urlpatterns = [
    path('tdashboard', views.Teacherdashboard.as_view(), name="teacherdashboard"),
    path('attendance', views.AttendanceView.as_view(), name="attendance"),
]