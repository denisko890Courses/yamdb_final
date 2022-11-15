from rest_framework import serializers
import re

from .models import User


class SignUpSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email')

    def validate_username(self, value):
        regex = re.compile('^[a-z][a-z0-9_]+$')
        if not regex.search(value):
            raise serializers.ValidationError(
                'Недопустимое имя пользователя')
        if value == 'me':
            raise serializers.ValidationError(
                'Имя пользователя не может быть "me"')
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError(
                'Пользователь с таким username уже существует')
        return value

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                'Пользователь с таким email уже существует')
        return value


class CreateTokenSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=150)

    class Meta:
        model = User
        fields = ('username', 'mail_confirmation_code')


class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name',
                  'last_name', 'bio', 'role')
