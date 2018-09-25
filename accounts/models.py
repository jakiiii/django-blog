from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager
)


# Create your manager here.
class UserManager(BaseUserManager):
    def create_user(self, email, first_name=None, last_name=None, password=None, is_activate=True, is_staff=False, is_admin=False):
        if not email:
            raise ValueError('User must have an email address!')
        if not password:
            raise ValueError('User must have an password!')
        if not first_name:
            raise ValueError('User must have first name!')
        if not last_name:
            raise ValueError('User must have last name!')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name
        )

        user.set_password(password)
        user.staff = is_staff
        user.admin = is_admin
        user.is_activate = is_activate
        user.save(using=self._db)
        return user

    def create_staff(self, email, first_name=None, last_name=None, password=None):
        user = self.create_user(
            email,
            first_name=first_name,
            last_name=last_name,
            password=password,
            is_staff=True
        )
        return user

    def create_superuser(self, email, first_name, last_name, password):
        user = self.create_user(
            email,
            first_name=first_name,
            last_name=last_name,
            password=password,
            is_staff=True,
            is_admin=True
        )
        return user


# Create your models here.
class User(AbstractBaseUser):
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(verbose_name='Email', max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    objects = UserManager()

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    # @property
    # def is_active(self):
    #     return self.active
