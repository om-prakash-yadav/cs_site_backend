from django.contrib import admin
from .models import Faculty, Event, Staff, gallery , Feed
# Register your models here.
admin.site.register(Faculty)
admin.site.register(Staff)
admin.site.register(Event)
admin.site.register(gallery)
admin.site.register(Feed)

