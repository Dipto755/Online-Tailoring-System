from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(fabric_model)
admin.site.register(design_model)
admin.site.register(user_model)