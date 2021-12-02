from django.contrib import admin
from .models import Prescriber, Drug

# Register your models here.
admin.site.register(Prescriber)
admin.site.register(Drug)