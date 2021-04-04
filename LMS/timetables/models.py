from django.db import models
from django.contrib.auth.models import User


class Timetable(models.Model):
    ttname = models.CharField(max_length=200)
    ttpic = models.ImageField(upload_to='timetablespic')
    ttpdf = models.FileField(upload_to='timetablespdf')
