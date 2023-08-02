from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import PermissionsMixin, AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth import password_validation
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, user_id,password, **extra_fields):
        if not user_id:
            raise ValueError('must be set username')
        user_id = self.model.nomalize_username(user_id)
        user = self.model(user_id, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, user_id, password, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(user_id, password, **extra_fields)

    def create_superuser(self, user_id, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('superuser must have is_superuser=True')

        return self._create_user(user_id, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):

    user_id = models.CharField(
        max_length=50,
        unique=True,
    )
    user_pw = models.CharField(max_length=20)
    user_pw2 = models.CharField(max_length=20, default='')
    user_name = models.CharField(max_length=50)
    email_addr = models.EmailField(max_length=128, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    user_validate = models.BooleanField(default=False)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('admin_info')
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'account_active or is not disabled'
        )
    )

    object = UserManager()

    USERNAME_FIELD = 'user_id'

    #필수로 받고 싶은 필드를 넣기위한 소스
    REQUIRED_FIELDS = ['user_pw']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def clean(self):
        super().clean()
        self.user_id = self.__class__.object.normalize_userid(self.user_id)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self._password = raw_password

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self._password is not None:
            password_validation.password_changed(self._password, self)
            self._password = None