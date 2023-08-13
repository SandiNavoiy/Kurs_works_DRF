from rest_framework import generics

from users.models import User
from users.serializers import UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    # Контроллер для создания пользователя
    serializer_class = UserSerializer


class UserListAPIView(generics.ListAPIView):
    # Контроллер для списка пользователей
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserRetrieveAPIView(generics.RetrieveAPIView):
    # Контроллер для просмотра пользователя
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateAPIView(generics.UpdateAPIView):
    # Контроллер для обновления пользователя
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDestroyAPIView(generics.DestroyAPIView):
    # Контроллер для удаления пользователя
    queryset = User.objects.all()
