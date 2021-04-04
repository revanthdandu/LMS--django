from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Timetable

class Timetables(LoginRequiredMixin,View):
    login_url = ''
    redirect_field_name = 'redirect_to'

    def get(self, request):
        timetable = Timetable.objects.all()

        pk = request.GET.get("pk", None)
        if pk:
            timetable_obj = Timetable.objects.get(pk=pk)
        else:
            timetable_obj = None


        return render(request, 'LMSteacherdashboard/timetable.html', {'timetable': timetable, 'timetable_obj':timetable_obj})
