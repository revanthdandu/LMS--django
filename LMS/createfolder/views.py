from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import pandas as pd
import numpy as np
import os
from .models import get_file_path
# Create your views here.

def attendence_sheet(request):

    key = '2021-04-04/11:55PM/H3'

    # key_ = '2021-04-04/11:55PM/H2'

    path = os.path.join(settings.BASE_DIR, 'media', 'I', 'CSE', 'PFSD', 'A', 'attendance', 'B.tech_1-CSE-PFSD-A.xlsx')
    df = pd.read_excel(path, usecols=[1])



    # df[key_] = 'P'
    # df.to_excel(path, index=False)

    # df = df.loc[:, ['roll no:', 'names:']]

    return HttpResponse(df.to_html())