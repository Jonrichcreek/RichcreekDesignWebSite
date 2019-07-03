from django.contrib import admin
from .models import Portfolio

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'publish', 'category', 'pub_date')
    list_display_links = ('id', 'title')
    list_filter = ('pub_date', 'category')
    list_editable = ('publish',)
    search_fields = ('id', 'title', 'publish', 'pub_date', 'description', 'category' )
    list_per_page = 25
admin.site.register(Portfolio, PortfolioAdmin)

