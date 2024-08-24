from django.core.exceptions import ValidationError
from django.core.serializers import serialize
from rest_framework import viewsets, status
from rest_framework import permissions
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from social_core.pipeline.partial import partial

from .models import Profile, Position, Workshop
from .permissions import IsOwner, IsOwnerOrReadOnly, ModelPermissions
from .serializers import WorkShopCreateSerializer, ProfileRegistrationSerializer, PositionCreateSerializer, \
    ProfileSerializer


class WorkShopAPIViewSet(viewsets.ModelViewSet):
    """
    Конечная точка API, позволяющая просматривать и редактировать цеха.
    """
    queryset = Workshop.objects.all()
    serializer_class = WorkShopCreateSerializer
    permission_classes = [ModelPermissions]

class PositionAPIViewSet(viewsets.ModelViewSet):
    """
    Конечная точка API, позволяющая просматривать и редактировать должности.
    """
    queryset = Position.objects.all()
    serializer_class = PositionCreateSerializer
    permission_classes = [ModelPermissions]


class ProfileAPIViewSet(viewsets.ModelViewSet):
    """
    Конечная точка API, позволяющая просматривать и редактировать пользователей.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [ModelPermissions]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()

        # Получаем данные из запроса
        data = request.data

        # Пример валидации: проверка уникальности email
        email = data.get('email', instance.email)
        if Profile.objects.exclude(pk=instance.pk).filter(email=email).exists():
            raise ValidationError({"email": "Этот email уже используется."})

        # Обновляем поля экземпляра
        instance.username = data.get('username', instance.username)
        instance.email = email
        instance.phone = data.get('phone', instance.phone)
        instance.last_name = data.get('last_name', instance.last_name)
        instance.name = data.get('name', instance.name)
        instance.surname = data.get('surname', instance.surname)
        instance.birthday = data.get('birthday', instance.birthday)

        # Обработка поля position
        position_id = data.get('position')  # Получаем идентификатор позиции
        if position_id:
            try:
                instance.position = Position.objects.get(pk=position_id)  # Получаем экземпляр Position
            except Position.DoesNotExist:
                raise ValidationError({"position": "Указанная должность не существует."})
        else:
            instance.position = None  # Если position не передан, устанавливаем в None

            # Обработка обновления пароля
        new_password = data.get('password')  # Получаем новый пароль
        if new_password:
            instance.set_password(new_password)  # Устанавливаем новый пароль

        # Сохраняем обновленный экземпляр
        instance.save()

        # Возвращаем обновленные данные
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


