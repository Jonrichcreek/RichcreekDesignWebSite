from django.contrib import admin
from .models import Service
# Register your models here.

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'publish', 'list_date')
    list_display_links = ('id', 'title')
    list_filter = ('list_date',)
    list_editable = ('publish',)
    search_fields = ('id', 'title', 'publish', 'list_date', 'description' )
    list_per_page = 25

admin.site.register(Service, ServiceAdmin)