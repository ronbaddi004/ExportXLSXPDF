from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from user_mbe.serializers.user import UserRegistrationSerializer


class UserRegistrationCreateAPIView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserRegistrationSerializer
