from django.urls import path

from accounts.views import  UserRegisterView, UserLoginView,UserLogoutView,ChangePasswordView
 


urlpatterns = [
  

    path('logout',  UserLogoutView.as_view(), name='logout'),
    path('login', UserLoginView.as_view() , name='login'),
    path('registr', UserRegisterView.as_view(), name='registr'),
    path('changepassword', ChangePasswordView.as_view(), name='changepassword'),
]