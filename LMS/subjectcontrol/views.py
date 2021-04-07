from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Notes, NotesFiles
from .models import Assignments



class Subjectcontrol(LoginRequiredMixin, View):

    login_url = ''
    redirect_field_name = 'redirect_to'

    def get(self, request):
        subject_files_list = request.user.profile.subject_control_list.all()
        assignments_upload_list = request.user.profile.assignments_upload_list.all()
        return render(request, 'LMSteacherdashboard/subcontrol.html', {'subject_control_list':subject_files_list,'assignments_upload_list':assignments_upload_list})

    def post(self, request):
        columnname=request.POST['notescolumnname']
        Notes.objects.create(
            profile = request.user.profile,
            name = columnname
        )

        return redirect('subjectcontrol')




class Assignments(LoginRequiredMixin, View):

    login_url = ''
    redirect_field_name = 'redirect_to'

    def get(self, request):
        assignments_upload_list = request.user.profile.assignments_upload_list.all()
        return render(request, 'LMSteacherdashboard/subcontrol.html', {'assignments_upload_list':assignments_upload_list})

    def post(self, request):
        columnname=request.POST['assignmentscolumnname']
        Assignments.objects.create(
            profile = request.user.profile,
            name = columnname
        )

        return redirect('uploadassignment')





class FileUpload(LoginRequiredMixin, View):


    login_url = ''
    redirect_field_name = 'redirect_to'

    def get(self, request, pk):
        return render(request, 'LMSteacherdashboard/addfiles.html')

    def post(self, request, pk):
        subject_control = Notes.objects.get(id=pk)
        file = request.FILES['subject_file']
        NotesFiles.objects.create(
            subject_control=subject_control,
            file=file,
            name="Revanth",
        )

        return redirect('subjectcontrol')


