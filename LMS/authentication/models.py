from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    DESIGNATION_CHOICE=[
        ('student','Student'),
        ('faculty', 'Faculty'),
        ('admin', 'Admin'),
    ]
    YEAR_CHOICE = [
        ('-', '-'),
        ('I', 'B.tech I year'),
        ('II', 'B.tech II year'),
        ('III', 'B.tech III year'),
        ('IV', 'B.tech IV year'),
    ]
    GENDER_CHOICE = [
        ('-', '-'),
        ('MALE', 'MALE'),
        ('FEMALE', 'FEMALE'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profilepic = models.ImageField(upload_to='profilepics')
    designation = models.CharField(max_length=50,choices=DESIGNATION_CHOICE,default='student')
    subject = models.CharField(max_length=200)
    branch = models.CharField(max_length=100)
    section = models.CharField(max_length=15)
    phone = models.CharField(max_length=15)
    year = models.CharField(max_length=100, choices=YEAR_CHOICE, default='-')
    gender = models.CharField(max_length=100, choices=GENDER_CHOICE, default='-')
    dateofbirth = models.DateField()
    fathername = models.CharField(max_length=100)
    fatherphone = models.CharField(max_length=15)
    address = models.TextField()
    city = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.user.username}"

