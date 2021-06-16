from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class DonatorInfo(models.Model):
	d_name = models.CharField(max_length=100, blank=True, null=True, default="")
	d_address = models.TextField(blank=True, null=True, default="")
	d_contact = models.PositiveIntegerField(validators=[
            MaxValueValidator(99999999999),
            MinValueValidator(0)
        ])
	d_email = models.EmailField(blank=True, null=True, max_length=254)
	class meta:
		db_table = "Donator's Information"

class Donation(models.Model):
	donator_id = models.ForeignKey(DonatorInfo, on_delete=models.CASCADE)
	item_name = models.CharField(max_length=75, default="")
	quantity_no = models.PositiveIntegerField(default=0)
	quantity_description = models.CharField(max_length=10, default="")
	date_donated = models.DateField(auto_now_add=False, auto_now=False)
	class meta:
		db_table = "List of Donation"
 
class ReceiverInfo(models.Model):
	r_name = models.CharField(max_length=100, default="")
	r_contact = models.PositiveIntegerField(validators=[
            MaxValueValidator(99999999999),
            MinValueValidator(0)
        ])
	r_address = models.TextField(default="")
	class meta:
		db_table = "Receiver's Information"
	
class ReceivedDonations(models.Model):
	received_id = models.ForeignKey(ReceiverInfo, on_delete=models.CASCADE)
	item_received = models.CharField(max_length=75, default="")
	r_quantity = models.PositiveIntegerField(default=0)
	r_quantitydescription = models.CharField(max_length=10, default="")
	item_status = models.CharField(max_length=30, default="")
	date_received = models.DateField(auto_now_add=False, auto_now=False)
	class meta:
		db_table = "Received Donations"
	
class ReceiverFeedback(models.Model):
	rdetails_id = models.ForeignKey(ReceiverInfo, on_delete=models.CASCADE)
	rdetails_ids = models.ForeignKey(ReceivedDonations, on_delete=models.CASCADE)
	RATING_CHOICES =(
		('Very Satisfied', 5),
		('Satisfied', 4),
		('Neutral', 3),
		('Disssatisfied', 2),
		('Very Disssatisfied', 1),
		)
	rating = models.IntegerField(choices=RATING_CHOICES, default='Neutral')
	comments = models.TextField(blank=True, null=True, default="")
	Suggestions = models.TextField(blank=True, null=True, default="")
	class meta:
		db_table = "Receiver Feedback"

class DonationStatus(models.Model):
	donation_id = models.ForeignKey(Donation, on_delete=models.CASCADE)
	quantity_stock = models.PositiveIntegerField(default=0)
	quantity_description = models.CharField(max_length=10, default="")
	DONATION_STATUSES = (
		('SPOILED', 'Spoiled'),
		('OUT OF STOCK', 'Out of Stock'),
		('AVAILABLE', 'Available'),
		)
	donation_status = models.CharField(choices=DONATION_STATUSES, max_length=12, default='AVAILABLE')
	class meta:
		db_table = "Donation Status"
# Create your models here.
