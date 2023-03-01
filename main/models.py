from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# class User(AbstractUser):
    # birth_date = models.DateField(auto_now=False, null=True)


class User(AbstractUser):
    # add this to avoid reverse accessor name clashes
    groups = models.ManyToManyField(Group, related_name='custom_user_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_set', blank=True)
