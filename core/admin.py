from django.contrib import admin
from core.models import Event


# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'date_event', 'date_create')
    list_filter = ('users','date_event','id',)


admin.site.register(Event, EventAdmin)
