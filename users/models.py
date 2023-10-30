from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.

class AccountManager(BaseUserManager):
    def create_user(self, firstname, lastname, username, email, password=None):
        if not email:
            raise ValueError('Provided Email Address is empty, please provide an Email.')
        if not username:
            raise ValueError('Provided Username is empty, please provide a Username.')
        user = self.model(
            email=self.normalize_email(email),  # change domain to be lowercase.
            firstname=firstname,
            lastname=lastname,
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, firstname, lastname, username, email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            firstname=firstname,
            lastname=lastname,
            password=password
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_super_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    objects = AccountManager()
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    # ACL roles
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_super_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'firstname', 'lastname']

    object = AccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True
