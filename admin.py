from django.contrib import admin
from home.models import  CollegeEvent, EventAdvisor, PartiesEvent, TechnicalEvent, WeddingEvent

from home.models import Contact

# Register your models here.
admin.site.register(Contact)
admin.site.register(EventAdvisor)
admin.site.register(WeddingEvent)
admin.site.register(PartiesEvent)
admin.site.register(CollegeEvent)
admin.site.register(TechnicalEvent)


