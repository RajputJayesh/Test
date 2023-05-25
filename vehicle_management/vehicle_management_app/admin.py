from django.contrib import admin
from vehicle_management_app.models import record
# Register your models here.

class recordadmin(admin.ModelAdmin):

    list_display=['num','vehicletype','vehiclemodel','vehicledes']

admin.site.register(record,recordadmin)
admin.site.site_header="Vehicle Management"