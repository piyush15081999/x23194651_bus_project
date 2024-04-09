from django.contrib import admin
from .models import Bus, Reservation, Srcdst
# Register your models here.

admin.site.register(Bus)
admin.site.register(Reservation)
admin.site.register(Srcdst)