from django.contrib import admin
from django.contrib.auth.models import Group

from api.models import User, Object

admin.site.register(User)
admin.site.register(Group)
admin.site.register(Object)
