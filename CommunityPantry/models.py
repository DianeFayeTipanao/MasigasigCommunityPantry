from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

'''class Donation(models.Model):
	item_name = models.CharField(max_length=75, default="")
	quantity_no = models.PositiveIntegerField(default=0)
	quantity_description = models.CharField(max_length=10, default="")
	date_donated = models.DateField(auto_now_add=False, auto_now=False)

	def __str__(self):
		return self.item_name

class DonatorInfo(models.Model):
	donator_id = models.ManytoManyField(Donation)
	d_name = models.CharField(max_length=100, blank=True, null=True, default="")
	d_address = models.TextField(blank=True, null=True, default="")
	d_contact = models.PositiveIntegerField(blank=True, null=True, max_length=11)
	d_email = models.EmailField(blank=True, null=True, max_length=254)
	 
	AFFILIATION_CHOICES = (
		('ALUMNI','Alumni'), 
		('FACULTY','Faculty'),
		('ADMIN', 'Admin'),
		('STUDENT', 'Student'),
		('NONE', 'None'),
		)
	d_affiliation = models.CharField(choices=AFFILIATION_CHOICES, default='NONE')'''

class ReceiverInfo(models.Model):
	r_name = models.CharField(max_length=100, default="")
	r_contact = models.PositiveIntegerField(validators=[
            MaxValueValidator(99999999999),
            MinValueValidator(0)
        ])
	r_address = models.TextField(default="")
	RAFFILIATION_CHOICES = (
		('ALUMNI','Alumni'), 
		('FACULTY','Faculty'),
		('ADMIN', 'Admin'),
		('STUDENT', 'Student'),
		('NONE', 'None'),
		)
	r_affiliation = models.CharField(choices=RAFFILIATION_CHOICES, max_length=7, default='NONE')
	
	def __str__(self):
		return self.r_name

class ReceivedDonations(models.Model):
	received_id = models.ForeignKey(ReceiverInfo, on_delete=models.CASCADE)
	item_received = models.CharField(max_length=75, default="")
	r_quantity = models.PositiveIntegerField(default=0)
	r_quantitydescription = models.CharField(max_length=10, default="")
	item_status = models.CharField(max_length=30, default="")
	date_received = models.DateField(auto_now_add=False, auto_now=False)

	def __str__(self):
		return self.receiver_id.r_name

'''class ReceiverFeedback(models.Model):
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

	def __str__(self):
		return self.rdetails_id.rating

class DonationStatus(models.Model):
	donation_id = models.ForeignKey(Donation, on_delete=models.CASCADE)
	
	def stock_check(self):
		quantity_stock = self.quantity_no - self.r_quantity
		return int(quantity_stock)

	quantity_description = models.CharField(max_length=10, default="")
	DONATION_STATUSES = (
		('SPOILED', 'Spoiled'),
		('OUT OF STOCK', 'Out of Stock'),
		('AVAILABLE', 'Available'),
		)
	donation_status = models.CharField(choices=DONATION_STATUSES, default='AVAILABLE')
	def __str__(self):
		return self.donation_id.item_name'''

# Create your models here.
