from django.contrib import admin
from events.models import Event


admin.site.site_header = "Events Admin"
admin.site.register(Event)
