from django.shortcuts import render
from django.views import View
from todo.models import Todo
from authentication.models import Profile



class Studentdashboard(View):
    def get(self, request):
        todos = Todo.objects.filter(user=request.user)
        return render(request, 'LMSstudentdashboard/dashboard.html', {'todos' : todos})


class Studentsubject(View):
    def get(self, request, subject):
        profile = Profile.objects.get(subject=subject)
        subject_files_list = profile.subject_control_list.all()
        assignments_upload_list = profile.assignments_upload_list.all()
        return render(request, 'LMSstudentdashboard/subjectpage.html', {'subject_control_list':subject_files_list,'assignments_upload_list':assignments_upload_list})
