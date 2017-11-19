from django.contrib import admin

from .models import Asset, Employee, Location, Manufacturer, Organization

admin.site.register(Asset)
admin.site.register(Employee)
admin.site.register(Location)
admin.site.register(Manufacturer)
admin.site.register(Organization)
