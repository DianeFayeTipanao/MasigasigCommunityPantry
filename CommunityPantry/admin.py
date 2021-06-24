from django.contrib import admin
from .models import DonatorInfo, Donation, ReceiverInfo, ReceivedDonations, ReceiverFeedback

admin.site.register(DonatorInfo)
admin.site.register(Donation)
admin.site.register(ReceiverInfo)
admin.site.register(ReceivedDonations)
admin.site.register(ReceiverFeedback)

# Register your models here.
