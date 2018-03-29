from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
    )


# Create your models here.

class UserProfileManager(BaseUserManager):
    """Used to work with custom user model"""
    def create_user(self, email, name, password=None):
        """Create a new user profile object"""

        if not email:
            raise ValueError('User must have an email address')

        email = self.normailized_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return users

    def create_superuser(self, email, name, password):
        """Creates and save a new superuser"""

        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_starff = True

        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Represents a "user profile" inside our system"""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_activate = models.BooleanField(default=True)
    is_starff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Used to get a users full name."""
        return self.name

    def get_short_name(self):
        """Used to get a short name"""
        return self.name

    def __str__(self):
        """ to show object as string"""
        return self.email
