from django.urls import path
from . import views

urlpatterns = [
    path('subjectcontrol', views.Subjectcontrol.as_view(), name="subjectcontrol"),
    path('uploadassignment', views.AssignmentsView.as_view(), name="uploadassignment"),
    path('notesupload/<int:pk>', views.NotesUpload.as_view(), name="notesupload"),
    path('assignmentsupload/<int:pk>', views.AssignmentsUpload.as_view(), name="assignmentsupload"),


]