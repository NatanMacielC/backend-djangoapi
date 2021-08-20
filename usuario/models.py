from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth import get_user_model
from django.utils import timezone


from Cliente.models import Cliente

# Create your models here.

class MyUserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        values = [email, password]
        field_value_map = dict(zip(self.model.REQUIRED_FIELDS, values))
        for field_name, value in field_value_map.items():
            if not value:
                raise ValueError('The {} value must be set'.format(field_name))

        user = self.model(
			email=self.normalize_email(email),
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):     
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password)


class Usuario(AbstractBaseUser, PermissionsMixin):

    ID = models.AutoField(primary_key=True, null=False, editable=False)

    Nome = models.CharField(max_length=150, null=False)

    email = models.EmailField(verbose_name="email", max_length=150, null=False, unique=True)

    CPF = models.CharField(max_length=20, null=False)

    Telefone = models.CharField(max_length=20, null=True)

    Celular = models.CharField(max_length=20, null=True)

    NomeUsuario = models.CharField(max_length=50, null=False)

    DataCadastro = models.DateField(auto_now_add=True, editable=False, null=False)

    DataAlteracao = models.DateField(auto_now=True, null=True)

    Ativo = models.BooleanField(default=True, null=True)

    Perfil = models.CharField(max_length=50, null=True)

    is_admin = models.BooleanField(default=False)

    is_staff = models.BooleanField(default=False)

    is_superuser = models.BooleanField(default=False)

    objects = MyUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['']

    def __str__(self):
        return self.Nome
    
    def has_perm(self):
        # perm, obj
        return self.is_admin
    
    def has_module_perms(self, app_module):
    	return True
        
        
        



