from django.contrib import admin
from .models import ReceiverInfo, ReceivedDonations

admin.site.register(ReceiverInfo)
admin.site.register(ReceivedDonations)

# Register your models here.
