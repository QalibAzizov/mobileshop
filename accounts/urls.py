from django.urls import path, include ,re_path
from accounts.views import (
    UserRegisterView,
    UserLoginView,
    UserLogoutView,
    ChangePasswordView,
    CustomPasswordResetView,
    CustomPasswordResetConfirmView
) 
 


urlpatterns = [
  
    path('forget-password', CustomPasswordResetView.as_view(),name='password-reset'),
    path('logout',  UserLogoutView.as_view(), name='logout'),
    path('login', UserLoginView.as_view() , name='login'),
    path('registr', UserRegisterView.as_view(), name='registr'),
    path('changepassword', ChangePasswordView.as_view(), name='changepassword'),
    re_path(r'^reset-password/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,33})/$',
    CustomPasswordResetConfirmView.as_view(), name='reset-password'),
]