from django.db import models    # noqa
from django.utils.translation import gettext_lazy as _

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    """Manager for user model"""
    def create_user(self, email, password=None, **extra_fields):
        """Create and save a new user"""

        if not email:
            raise ValueError('Email field could not be empty.')

        user = self.model(
            email=self.normalize_email(email),
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create and save and return a new superuser"""

        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user
class User(AbstractBaseUser, PermissionsMixin):

    """Custom user model that supports using email instead of username """

    email = models.EmailField(max_length=255, unique=True, verbose_name=_('email address'))
    name = models.CharField(max_length=255, verbose_name=_('name'))
    is_active = models.BooleanField(default=True, verbose_name=_('is active'))
    is_staff = models.BooleanField(default=False, verbose_name=_('is staff'))

    objects = UserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')