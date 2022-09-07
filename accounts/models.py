from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy

from django.contrib.auth.models import AbstractUser




class User(AbstractUser):
    pass

class AbsrtactModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Subscriber(AbsrtactModel):
    email = models.EmailField('Email',unique=True,max_length=40)
    is_active = models.BooleanField('Is Active', default = True)

    def __str__(self) :
        return self.email

    class Meta:
        verbose_name = 'Suscriber'
        verbose_name_plural = 'Suscribers'  