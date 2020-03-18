from django.contrib import admin
from light.models import Light

class LightAdmin(admin.ModelAdmin):
    list_display=['color', 'state']

admin.site.register(Light, LightAdmin)