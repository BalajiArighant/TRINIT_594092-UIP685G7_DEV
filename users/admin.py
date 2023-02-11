from django.contrib import admin
from .models import user, NGO, Projects

# Register your models here.

admin.site.register(user)
admin.site.register(NGO)
admin.site.register(Projects)