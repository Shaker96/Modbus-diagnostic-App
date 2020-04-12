from django.contrib import admin

# Register your models here.
from .models import Register, Reading, Actuator, Value, Log

admin.site.register(Register)
admin.site.register(Actuator)
admin.site.register(Reading)
admin.site.register(Value)
admin.site.register(Log)
