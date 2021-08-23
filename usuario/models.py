from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth import get_user_model
from django.utils import timezone
from cliente.models import Cliente

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
    id = models.AutoField(db_column='ID', primary_key=True) 
    nome = models.CharField(db_column='Nome',max_length=150, null=False)
    email = models.EmailField(db_column='Email', max_length=150, null=False, unique=True)
    cpf = models.CharField(db_column='CPF', max_length=20, null=False)
    telefone = models.CharField(db_column='Telefone', max_length=20, null=True)
    celular = models.CharField(db_column='Celular', max_length=20, null=True)
    nomeusuario = models.CharField(db_column='NomeUsuario', max_length=50, null=False)
    datacadastro = models.DateField(db_column='DataCadastro', auto_now_add=True, null=False, blank=False)
    dataalteracao = models.DateField(db_column='DataAlteracao', auto_now=True, null=True, blank=True)
    ativo = models.BooleanField(db_column='Ativo', default=True, null=True, blank=True)
    perfil = models.CharField(db_column='Perfil', max_length=50)

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

        
        
        



