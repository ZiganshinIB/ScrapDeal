from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from rest_framework import serializers

from .models import Profile, Workshop, Position

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'username',
            'email',
            'name',
            'last_name',
            'surname',
            'phone',
            'work_phone',
            'birthday',
            'position',
            'photo',
            'date_joined',
            'password')

        extra_kwargs = {
            'password': {'write_only': True, 'required': False},
            'name': {'required': True},
            'last_name': {'required': True},
            'surname': {'required': False},
            'phone': {'required': False},
            'position': {'required': False},
            'work_phone': {'required': False},
            'birthday': {'required': False},
            'photo': {'required': False},
            'date_joined': {'read_only': True}
        }

        def create(self, validated_data):
            return Profile.objects.create_user(**validated_data)

        def update(self, instance, validated_data):
            if 'password' in validated_data:
                password = validated_data.pop('password')
                instance.set_password(password)
            instance.name = validated_data.get('name', instance.name)
            instance.last_name = validated_data.get('last_name', instance.last_name)
            instance.surname = validated_data.get('surname', instance.surname)
            instance.phone = validated_data.get('phone', instance.phone)
            instance.position = validated_data.get('position', instance.position)
            instance.work_phone = validated_data.get('work_phone', instance.work_phone)
            instance.birthday = validated_data.get('birthday', instance.birthday)
            instance.photo = validated_data.get('photo', instance.photo)
            instance.save()
            return instance



class ProfileRegistrationSerializer(BaseUserCreateSerializer):
    # Secret Password


    class Meta(BaseUserCreateSerializer.Meta):
        model = Profile
        fields = (
            'username',
            'email',
            'name',
            'last_name',
            'surname',
            'phone',
            'work_phone',
            'birthday',
            'position',
            'photo',
            'date_joined'
            'password')
        extra_kwargs = {
            'password': {'required': True},
            'name': {'required': True},
            'last_name': {'required': True},
            'surname': {'required': False},
            'phone': {'required': False},
            'position': {'required': False},
            'work_phone': {'required': False},
            'birthday': {'required': False},
            'photo': {'required': False},
            'date_joined': {'read_only': True}

        }

    def create(self, validated_data):
        user = super().create(validated_data)
        user.is_active = True
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.surname = validated_data.get('surname', instance.surname)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.position = validated_data.get('position', instance.position)
        instance.work_phone = validated_data.get('work_phone', instance.work_phone)
        instance.birthday = validated_data.get('birthday', instance.birthday)
        instance.photo = validated_data.get('photo', instance.photo)
        instance.save()
        return instance



class WorkShopCreateSerializer(serializers.ModelSerializer):
    """ Сеариализация Цеха model: account.Workshop"""
    positions = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Workshop
        fields = ('number', 'name', 'head', 'positions')


class PositionCreateSerializer(serializers.ModelSerializer):
    """ Сеариализация должности model: account.Position"""
    profiles = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Position
        fields = ('title', 'workshop', 'profiles')