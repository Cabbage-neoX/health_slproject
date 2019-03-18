from django.contrib import admin
# Register your models here.
from . import models

admin.site.register(models.User)
admin.site.register(models.Doctor)
admin.site.register(models.Diagnostic_results)
admin.site.register(models.Doctor_to_user)