from django.contrib import admin
from .models import Crystal, Charging, Lore


# Register your models here.
admin.site.register(Crystal)
admin.site.register(Charging)
admin.site.register(Lore)