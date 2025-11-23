from django.contrib import admin
from .models import * 

# Register your models here.
admin.site.register(User)
admin.site.register(Room)
admin.site.register(module)
admin.site.register(cohort)
admin.site.register(Booking)