from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .models import Todo

# Create your views here.
class CreateTodo(LoginRequiredMixin, View):
    login_url = ''
    redirect_field_name = 'redirect_to'

    def get(self, request):
        todo_list = Todo.objects.filter(user=request.user)
        # todo_list = request.user.todo_set.all()
        context = {
            'todo_list': todo_list
        }
        return render(request, 'todo/create.html', context)

    def post(self, request):
        task = request.POST['task']
        date = request.POST['date']
        time = request.POST['time']

        todo = Todo.objects.create(
            task=task,
            date=date,
            time=time,
            user=request.user
        )

        return redirect('profile')


class DeleteTodo(LoginRequiredMixin, View):
    login_url = ''
    redirect_field_name = 'redirect_to'

    def get(self, request, pk):
        todo = Todo.objects.get(pk=pk)

        if todo.user == request.user:
            todo.delete()
            return redirect("teacherdashboard")
        else:
            return redirect("teacherdashboard")