from django.db import models

# Create your models here.

def get_file_path(instance, filename):
    year = instance.year
    branch = instance.branch
    subject = instance.subject
    section = instance.section

    return f"{year}/{branch}/{subject}/{section}/attendance/{filename}"

# def notes(instance,filename):
#     year = instance.year
#     branch = instance.branch
#     subject = instance.subject
#     section = instance.section
#
#     return f"{year}/{branch}/{subject}/{section}/notes/{filename}"

class Attendance(models.Model):
    YEAR_CHOICES = [
        ('I', 'B.Tech 1'),
        ('II', 'B.Tech 2'),
    ]

    year = models.CharField(max_length=100, choices=YEAR_CHOICES, default='I')
    branch = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    section = models.CharField(max_length=10)

    excel_sheet  = models.FileField(upload_to=get_file_path)


# class Notes(models.Model):
#     YEAR_CHOICES = [
#         ('I', 'B.Tech 1'),
#         ('II', 'B.Tech 2'),
#     ]
#
#     year = models.CharField(max_length=100, choices=YEAR_CHOICES, default='I')
#     branch = models.CharField(max_length=200)
#     subject = models.CharField(max_length=200)
#     section = models.CharField(max_length=10)
#     excel_sheet  = models.FileField(upload_to=f"{year}/{branch}/{subject}/{section}/notes/{filename}")