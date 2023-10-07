from django.contrib import admin

# Register your models here.

from .models import fabric_model, design_model

admin.site.register(fabric_model)
admin.site.register(design_model)