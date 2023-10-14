from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(fabric_model)
admin.site.register(design_kameez_model)
admin.site.register(design_salowaar_model)
admin.site.register(design_shirt_model)
admin.site.register(user_model)