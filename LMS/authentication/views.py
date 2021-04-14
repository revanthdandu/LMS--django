from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin



# class Register(View):
#     def get(self, request):
#         return render(request, 'authentication/register.html')
#
#     def post(self, request):
#         user_name = request.POST['user_name']
#         email = request.POST['email']
#         password = request.POST['password']
#
#         user = User.objects.create_user(
#             username=user_name,
#             email=email,
#             password=password
#         )
#
#         # user.save()
#
#         return redirect('login')

class Login(View):
    def get(self, request):
        return render(request, 'teacherloginpage/login.html')

    def post(self, request):
        user_name = request.POST['user_name']
        password = request.POST['password']

        user = authenticate(request, username=user_name, password=password)

        if user is not None:
            login(request, user)
            if user.profile.designation == 'faculty':
                return redirect('teacherdashboard')
            if user.profile.designation == 'student':
                return redirect('studentdashboard')
        else:
            return redirect('login')

def logout_user(request):
    logout(request)
    return redirect('login')

class Profile_user(LoginRequiredMixin, View):

    login_url = ''
    redirect_field_name = 'redirect_to'

    def get(self, request):
        return render(request, 'LMSteacherdashboard/profile.html')

class Update_address(LoginRequiredMixin, View):
    login_url = ''
    redirect_field_name = 'redirect_to'

    def post(self, request):
        address = request.POST['address']
        city = request.POST['city']
        phonenumber = request.POST['phonenumber']

        request.user.profile.address = address
        request.user.profile.city = city
        request.user.profile.phone = phonenumber
        request.user.profile.save()

        return redirect("profile")

class Update_profilepic(LoginRequiredMixin, View):
    login_url = ''
    redirect_field_name = 'redirect_to'

    def post(self, request):
        profilepic = request.FILES['profilepic']
        request.user.profile.profilepic = profilepic
        request.user.profile.save()

        return redirect("profile")

class Delete_profilepic(LoginRequiredMixin, View):
    login_url = ''
    redirect_field_name = 'redirect_to'

    def get(self, request):
        request.user.profile.profilepic.delete()

        return redirect("profile")


class Change_password(LoginRequiredMixin, View):
    login_url = ''
    redirect_field_name = 'redirect_to'

    def post(self, request):
        currentpassword = request.POST['currentpassword']
        newpassword = request.POST['newpassword']
        repeatpassword = request.POST['repeatpassword']

        user = authenticate(request, username=request.user.username, password=currentpassword)
        if user is not None:
            if newpassword == repeatpassword:
                request.user.set_password(newpassword)
                request.user.save()
            else:
                raise Exception("Passwords didn't match")


        return logout_user(request)
