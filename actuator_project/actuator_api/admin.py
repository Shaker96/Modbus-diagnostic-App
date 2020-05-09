from django.contrib import admin

# Register your models here.
from .models import Register, Reading, Actuator, Value, CustomUser, Log

class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Register)
admin.site.register(Reading)
admin.site.register(Actuator)
admin.site.register(Value)
admin.site.register(Log)
# admin.site.register(ActuatorAlert)
