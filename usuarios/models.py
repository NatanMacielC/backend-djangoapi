from enum import unique
from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.core import validators
import re
from django.conf import settings
from django.utils import timezone
from django.core.mail import send_mail


# Create your models here.

# superuser
class UserManager(BaseUserManager):
    def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        if not username:
            raise ValueError(_('The given username must be set'))
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, is_staff=is_staff, is_active=True, is_superuser=is_superuser, last_login=now, date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        return self._create_user(username, email, password, False, False, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        user=self._create_user(username, email, password, True, True, **extra_fields)
        user.is_active=True
        user.save(using=self._db)
        return user


# usuário
class User(AbstractUser):

    ID = models.UUIDField(_("User UUID"), editable=False, default=uuid.uuid4)

    Nome = models.CharField(max_length=150, null=False)

    Email = models.EmailField(max_length=150, null=False, unique=True)

    CPF = models.CharField(max_length=20, null=False)

    Telefone = models.CharField(max_length=20, null=True)

    Celular = models.CharField(max_length=20, null=True)

    NomeUsuario = models.CharField(max_length=150, null=False)

    ClienteID = models.UUIDField(_("User UUID"), editable=False, default=uuid.uuid4)

    DataCadastro =  models.DateField(auto_now_add=True)

    DataCadastro =  models.DateField(null=True)

    is_trusty = models.BooleanField(_('trusty'), default=False,
 help_text=_('Designates whether this user has confirmed his account.'))

    Ativo = models.BooleanField(default=True, null=True)

    Perfil = models.CharField(max_length=150, null=False)

    Senha = models.CharField(max_length=50, null=True)



    USERNAME_FIELD = 'Email'
    REQUIRED_FIELDS = ['Nome', 'CPF', 'NomeUsuario']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
    def get_full_name(self):
        full_name = '%s %s' % (self.nome)
        return full_name.strip()