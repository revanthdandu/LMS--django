from django.urls import path
from . import views

urlpatterns = [
    path('', views.attendence_sheet, name="attendance"),

]