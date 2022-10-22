from django.contrib import admin
from .models import Destination

# Register your models here.
# it add login destination in django admin panel for login
admin.site.register(Destination)