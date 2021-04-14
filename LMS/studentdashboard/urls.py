from django.urls import path
from . import views

urlpatterns = [
    path('sdashboard', views.Studentdashboard.as_view(), name="studentdashboard"),
    path('studentsubject/<str:subject>', views.Studentsubject.as_view(), name="studentsubject"),
]