from django.shortcuts import render
from django.views import View
from todo.models import Todo


class Teacherdashboard(View):
    def get(self, request):
        todos = Todo.objects.filter(user=request.user)
        return render(request, 'LMSteacherdashboard/dashboard.html', {'todos' : todos})
