from django.urls import path
from . import views

urlpatterns = [
    path('tts', views.Timetables.as_view(), name="tts"),
]