from django.contrib import admin
from .models import SystemConfiguration

class SystemConfigurationAdmin(admin.ModelAdmin):
    model: SystemConfiguration
    list_display = ['codigo', 'descricao']
    search_fields = ['codigo']
    list_filter = ['codigo']
    save_on_top = True

admin.site.register(SystemConfiguration, SystemConfigurationAdmin)
