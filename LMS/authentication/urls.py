from django.urls import path
from . import views

urlpatterns = [
    path('', views.Login.as_view(), name="login"),
    path('logout', views.logout_user, name="logout"),
    path('profile', views.Profile_user.as_view(), name="profile"),
    path('updateaddress', views.Update_address.as_view(), name="updateaddress"),
    path('updateprofilepic', views.Update_profilepic.as_view(), name="updateprofilepic"),
    path('deleteprofilepic', views.Delete_profilepic.as_view(), name="deleteprofilepic"),
    path('changepassword', views.Change_password.as_view(), name="changepassword"),

]