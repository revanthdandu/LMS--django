from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import SubjectControl



class Subjectcontrol(LoginRequiredMixin, View):

    login_url = ''
    redirect_field_name = 'redirect_to'

    def get(self, request):
        subject_files_list = request.user.profile.subject_control_list.all()
        return render(request, 'LMSteacherdashboard/subcontrol.html', {'subject_control_list':subject_files_list})

    def post(self, request):
        columnname=request.POST['notescolumnname']
        SubjectControl.objects.create(
            profile = request.user.profile,
            name = columnname
        )

        return redirect('subjectcontrol')


