from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Doubles)
admin.site.register(models.MixedDoubles)
admin.site.register(models.DoublesWithNoPartner)
admin.site.register(models.Singles)
