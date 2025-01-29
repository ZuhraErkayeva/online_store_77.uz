from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError


class UserManager(BaseUserManager):
    def _create_user(self, password, phone_number, **extra_fields):
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        phone_number = extra_fields.pop('phone_number')
        password = extra_fields.pop('password')
        return self._create_user(phone_number=phone_number, password=password, **extra_fields)

    def create_superuser(self, password, phone_number, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', self.model.Role.ADMIN)

        if extra_fields.get('is_staff') is not True:
            raise ValidationError('Superuser must have is_staff=True')

        if extra_fields.get('is_superuser') is not True:
            raise ValidationError('Superuser must have is_superuser=True')
        return self._create_user(phone_number=phone_number, password=password, **extra_fields)

    def create_seller(self, data):
        data['role'] = self.model.Role.SELLER
        user = self.create_user(**data)
        return user

