from rest_framework import serializers
from .models import User
from .validators import PasswordValidator


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    gender = serializers.ChoiceField(choices=['М', 'Ж'])
    password = serializers.CharField(write_only=True, min_length=8, validators=[PasswordValidator()])
    password_confirm = serializers.CharField(write_only=True, min_length=8, validators=[PasswordValidator()])

    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError('Пароли не совпадают')
        return data

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User.objects.create_user(**validated_data, password=password)

        return user


from django.contrib.auth import get_user_model


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        User = get_user_model()
        user = User.objects.filter(username=username).first()

        if user is None:
            raise serializers.ValidationError("User not found")

        if not user.check_password(password):
            raise serializers.ValidationError("Invalid password")

        data['user'] = user
        return data
