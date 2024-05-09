from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, username, email, gender, password, password_confirm, **extra_fields):
        if not all([username, email, gender, password, password_confirm]):
            raise ValueError('Это поле не должно быть пустым!')

        user = self.model(
            username=username,
            email=email,
            gender=gender,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, gender, password,
                         **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        return self.create_user(username, email, gender, password, password,
                                **extra_fields)
