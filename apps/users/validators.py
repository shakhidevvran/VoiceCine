from rest_framework import serializers


class PasswordValidator:
    def __call__(self, value):
        # Проверка минимальной длины
        if len(value) < 8:
            raise serializers.ValidationError('Пароль должен содержать не менее 8 символов')




        # Проверка наличия хотя бы одной цифры
        if not any(char.isdigit() for char in value):
            raise serializers.ValidationError('Пароль должен содержать хотя бы одну цифру')