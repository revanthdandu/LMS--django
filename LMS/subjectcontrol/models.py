from django.db import models
from authentication.models import Profile

# Create your models here.
class Notes(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name='subject_control_list')
    name = models.CharField(max_length=150)

class NotesFiles(models.Model):
    file = models.FileField(upload_to='subjectcontrol/files')
    name = models.CharField(max_length=100)
    subject_control = models.ForeignKey(Notes, on_delete=models.CASCADE, related_name='subject_files_list')


class Assignments(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name='assignments_upload_list')
    name = models.CharField(max_length=150)

class AssignmentsFiles(models.Model):
    file = models.FileField(upload_to='assignmentsupload/files')
    name = models.CharField(max_length=100)
    assignment = models.ForeignKey(Assignments, on_delete=models.CASCADE, related_name='assignments_upload_list')