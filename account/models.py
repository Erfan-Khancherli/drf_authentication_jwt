from django.db import models
from django.contrib.auth.models import AbstractBaseUser , PermissionsMixin , BaseUserManager
# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self , email , first_name , last_name,password = None):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        if not first_name:
            raise ValueError("User must have a first name")
        if not last_name:
            raise ValueError("User must have a last name")
        
        user = self.model(email = self.normalize_email(email))
        user.first_name = first_name
        user.last_name  = last_name
        user.set_password(password)
        user.is_admin = False
        user.is_staff = False
        user.save()
        return user
    def create_superuser(self, email, first_name, last_name, password=None):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        if not first_name:
            raise ValueError("User must have a first name")
        if not last_name:
            raise ValueError("User must have a last name")

        user = self.model(
            email=self.normalize_email(email)
        )
        user.first_name = first_name
        user.last_name = last_name
        user.set_password(password)  # change password to hash
        user.is_admin = True
        user.is_staff = True
        user.save()
        return user
    
class CustomUser(AbstractBaseUser):
    ADMIN = 'admin'
    STAFF = 'staff'
    STAUS = [
        (ADMIN , ('Admin User')),
        (STAFF, ('Staff user')),
    ]
    email = models.EmailField(('email address') , unique =True)
    first_name = models.CharField(('first name'), max_length=30)
    last_name = models.CharField(('last name'), max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # a admin user; non super-user
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    @staticmethod
    def has_perm(perm, obj=None):
        # "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    @staticmethod
    def has_module_perms(app_label):
        # "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def __str__(self):
        return "{}".format(self.email)