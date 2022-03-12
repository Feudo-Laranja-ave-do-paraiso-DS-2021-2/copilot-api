from copilot.models import User
from django.contrib import admin

class Users(admin.ModelAdmin):
    list_display = ('id', 'nome', 'mac_address', 'latitude', 'longitude', 'hora')
    list_display_links = ('id', 'nome', 'mac_address', 'latitude', 'longitude', 'hora')
    search_fields = ('id', 'nome', 'mac_address', 'latitude', 'longitude', 'hora')

admin.site.register(User, Users)
