from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class DonatorInfo(models.Model):
	d_name = models.CharField(max_length=100, default="", blank=True, null=True)
	d_address = models.TextField(default="")
	d_contact = models.PositiveIntegerField(default =0, blank=True, null=True, validators=[
            MaxValueValidator(99999999999),
            MinValueValidator(0)
        ])
	d_email = models.EmailField(max_length=254, default="", blank=True, null=True)
	class meta:
		db_table = "Donator's Information"

class Donation(models.Model):
	donator_id = models.ForeignKey(DonatorInfo, default="", on_delete= models.CASCADE, blank=True, null=True)
	item_name = models.CharField(max_length=75, default="", blank=True, null=True)
	quantity_no = models.PositiveIntegerField(default=0, blank=True, null=True)
	quantity_description = models.CharField(max_length=10, default="", blank=True, null=True)
	date_donated = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
	class meta:
		db_table = "List of Donation"
 
class ReceiverInfo(models.Model):
	r_name = models.CharField(max_length=100, default="", blank=True, null=True)
	r_contact = models.PositiveIntegerField(default="", blank=True, null=True, validators=[
            MaxValueValidator(99999999999),
            MinValueValidator(0)
        ])
	r_address = models.TextField(default="", blank=True, null=True)
	class meta:
		db_table = "Receiver's Information"
	
class ReceivedDonations(models.Model):
	received_id = models.ForeignKey(ReceiverInfo, default="", on_delete= models.CASCADE, blank=True, null=True)
	item_received = models.CharField(max_length=75, default="", blank=True, null=True)
	r_quantity = models.PositiveIntegerField(default=0, blank=True, null=True)
	r_quantitydescription = models.CharField(max_length=10, default="", blank=True, null=True)
	item_status = models.CharField(max_length=30, default="", blank=True, null=True)
	date_received = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
	class meta:
		db_table = "Received Donations"
	
class ReceiverFeedback(models.Model):
	rdetails_id = models.ForeignKey(ReceiverInfo, on_delete=models.CASCADE, blank=True, null=True)
	rdetails_ids = models.ForeignKey(ReceivedDonations, on_delete=models.CASCADE, blank=True, null=True)
	RATING_CHOICES =(
		('Very Satisfied', 5),
		('Satisfied', 4),
		('Neutral', 3),
		('Disssatisfied', 2),
		('Very Disssatisfied', 1),
		)
	comments = models.TextField(blank=True, null=True, default="")
	Suggestions = models.TextField(blank=True, null=True, default="")
	class meta:
		db_table = "Receiver Feedback"

# Create your models here.
