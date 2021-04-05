# from django.shortcuts import render
# from django.views import View
# from django.conf import settings
# from django.http import HttpResponse
# import pandas as pd
# from .models import Attendance
# from django.db.models import Q
# import numpy as np
# import os
#
#
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
#
# # def attendence_sheet(request):
# #
# #     key = '2021-04-04/11:55PM/H3'
# #
# #     # key_ = '2021-04-04/11:55PM/H2'
# #
# #     path = os.path.join(settings.BASE_DIR, 'media', 'I', 'CSE', 'PFSD', 'A', 'attendance', 'B.tech_1-CSE-PFSD-A.xlsx')
# #     df = pd.read_excel(path, usecols=[1])
# #
# #
# #
# #     # df[key_] = 'P'
# #     # df.to_excel(path, index=False)
# #
# #     # df = df.loc[:, ['roll no:', 'names:']]
# #
# #     return HttpResponse(df.to_html())