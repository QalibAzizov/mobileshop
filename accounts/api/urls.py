from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


from accounts.api.views import UserProfileAPIView, SubscribersView

urlpatterns = [  
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('me/', UserProfileAPIView.as_view(), name='me'),  #user-profile
    path('subscribers', SubscribersView.as_view(),),


]