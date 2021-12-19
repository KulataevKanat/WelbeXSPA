from django.contrib.auth.models import Group, AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from api.managers import UserAccountManager
from WelbeXSPA.models import BaseModel


def role_null():
    return Group.objects.get_or_create(name='role_null')[0]


class User(BaseModel, AbstractUser):
    groups = models.ForeignKey(Group, on_delete=models.SET(role_null), null=True, blank=True)
    email = models.EmailField(max_length=50, unique=False, blank=True, null=True)

    objects = UserAccountManager()

    REQUIRED_FIELDS = ['groups_id', 'email']
    USERNAME_FIELD = 'username'
    REQUIRED_ADMIN_FIELDS = ['email']

    def __str__(self):
        return self.username.__str__()

    def get_full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    def get_short_name(self):
        return self.first_name

    class Meta:
        db_table = 'api_user'
        verbose_name = _('Пользоваетель')
        verbose_name_plural = _('Пользователи')


class Object(BaseModel):
    name = models.CharField(max_length=1000, blank=True, null=True)
    quantity = models.IntegerField(blank=False, default=0)
    distance = models.BigIntegerField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
