from django.shortcuts import render
from django.views import View
from todo.models import Todo
from django.conf import settings
from django.http import HttpResponse
import pandas as pd
from createfolder.models import Attendance
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
import json
import numpy as np
import os


class Teacherdashboard(View):
    def get(self, request):
        todos = Todo.objects.filter(user=request.user)
        return render(request, 'LMSteacherdashboard/dashboard.html', {'todos' : todos})

# class ExcelAttendance(View):
#
#     def get(self, request):
#         q1 = Q(year=request.GET['year'])
#         q2 =  Q(branch=request.GET['branch'])
#         q3 =  Q(subject=request.GET['subject'])
#         q4 =  Q(section=request.GET['section'])
#
#         attendance = Attendance.objects.get(q1 & q2 & q3 & q4)
#
#         df = pd.read_excel(attendance.excel_sheet)
#
#         return HttpResponse(df.to_html())

@method_decorator(csrf_exempt, name="dispatch")
class AttendanceView(View):


    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        q1 = Q(year=request.user.profile.year)
        q2 = Q(branch=request.user.profile.branch)
        q3 = Q(subject=request.user.profile.subject)
        q4 = Q(section=request.GET['section'])

        # print(request.GET.get("absent_list", []))

        date = request.GET['date']
        time = request.GET['time']
        hour = request.GET['hour']

        key = f'{date}/{time}/{hour}'

        attendance = Attendance.objects.get(q1 & q2 & q3 & q4)
        df = pd.read_excel(attendance.excel_sheet)
        absent_list = list(map(lambda x : int(x), data['absent_list']))

        # print(data['absent_list'])
        # print(df['roll no'].isin(absent_list))
        # print(df['roll no'])
        df.loc[df['roll no'].isin(absent_list), key] = 'A'
        print(df)

        df.to_excel(attendance.excel_sheet.path, index=False)
        return HttpResponse("ok")


    def get(self, request):

        try:
            q1 = Q(year=request.user.profile.year)
            q2 =  Q(branch=request.user.profile.branch)
            q3 =  Q(subject=request.user.profile.subject)
            q4 =  Q(section=request.GET['section'])

            print(request.GET.get("absent_list", []))

            date = request.GET['date']
            time = request.GET['time']
            hour = request.GET['hour']

            key = f'{date}/{time}/{hour}'

            attendance = Attendance.objects.get(q1 & q2 & q3 & q4)
            df = pd.read_excel(attendance.excel_sheet)

            if key not in df.columns:
                df[key] = 'P'
                df.to_excel(attendance.excel_sheet.path, index=False)
            # print(df.values)

            att_list = df.values
        except Exception as e:
            att_list = []

        return render(request, 'LMSteacherdashboard/attendance.html', {'att_list':att_list})