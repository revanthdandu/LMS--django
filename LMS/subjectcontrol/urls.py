from django.urls import path
from . import views

urlpatterns = [
    path('subjectcontrol', views.Subjectcontrol.as_view(), name="subjectcontrol"),
    path('uploadassignment', views.Assignments.as_view(), name="uploadassignment"),
    path('fileupload/<int:pk>', views.FileUpload.as_view(), name="fileupload"),

]