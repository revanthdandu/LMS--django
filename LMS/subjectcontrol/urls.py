from django.urls import path
from . import views

urlpatterns = [
    path('subjectcontrol', views.Subjectcontrol.as_view(), name="subjectcontrol"),


]