from enum import unique
from django.core.validators import RegexValidator
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



class User(AbstractUser):

    uuid = models.UUIDField(_("User UUID"), editable=False, default=uuid.uuid4)
    username = models.CharField(_('username'), max_length=15, unique=True, 
    help_text=_('Required. 15 characters or fewer. Letters, numbers and @/./+/-/_ characters'), 
    validators=[ validators.RegexValidator(re.compile('^[\w.@+-]+$'), _('Enter a valid username.'), _('invalid'))])

    nome = models.CharField(_('nome'), max_length=30, blank=False, null=False)

    email = models.EmailField(_('email'), max_length=255, unique=True, blank=False, null=False)

    cpf = models.CharField(_('CPF'), max_length=11, unique=True, blank=False, null=False)

    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")

    phoneNumber = models.CharField(_('telefone'),validators = [phoneNumberRegex], max_length = 16, unique = True)

    adPhoneNumber = models.CharField(_('celular'),validators = [phoneNumberRegex], max_length = 16, unique = True)

    create_at =  models.DateField(auto_now_add=True)

    is_trusty = models.BooleanField(_('trusty'), default=False,
 help_text=_('Designates whether this user has confirmed his account.'))



    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'nome', 'cpf', 'phoneNumber']

    objects = UserManager ()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
    def get_full_name(self):
        full_name = '%s %s' % (self.nome)
        return full_name.strip()

    def email_user(self, subject, message, from_email=None):
     send_mail(subject, message, from_email, [self.email])
