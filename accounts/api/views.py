from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveAPIView, CreateAPIView
from accounts.api.serializers import Userserializer,SubscribeSerializer


User = get_user_model()


class UserProfileAPIView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = Userserializer

    def get_object(self):
        return self.request.user


class SubscribersView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SubscribeSerializer