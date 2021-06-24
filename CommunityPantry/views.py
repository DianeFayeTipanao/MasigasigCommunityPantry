from django.shortcuts import render, redirect
from CommunityPantry.models import DonatorInfo, Donation, ReceiverInfo, ReceivedDonations, ReceiverFeedback
from .forms import DonationForm

def HomeBase(request):
	return render(request, 'home.html')
def Homepage(request):
	return render(request, 'home.html')

def donator(request):
	return render(request, 'DonatorSlip.html')
def createdonator(request):
	don=DonatorInfo.objects.create(
		d_name = request.POST['nameDName'], 
		d_contact = request.POST['nameDPhone'],
		d_address = request.POST['nameDAddress'],
		d_email = request.POST['nameDEmail'],
		)
	return render(request,'DonationSlip.html')
def createddonation(request):
	dntn=Donation.objects.create(
		item_name = request.POST['nameDIName'], 
		quantity_no = request.POST['nameDQNumber'],
		quantity_description = request.POST['nameDQDescription'],
		date_donated = request.POST['nameDDate'],
		)
	return render(request,'DonationSlip.html')
def displaydonation(request):
	dons=Donation.objects.all()
	context ={'dons':dons}
	return render(request,'DonationStatus.html', context)

def receiver(request):
	return render(request, 'ReceiverSlip.html')
def createdreceiver(request):
	rcvr=ReceiverInfo.objects.create(
		r_name = request.POST['nameRName'], 
		r_contact = request.POST['nameRPhone'],
		r_address = request.POST['nameRAddress'],
		)
	return render(request,'ReceivingSlip.html')
def createdreceived(request):
	rcvd=ReceivedDonations.objects.create(
		item_received = request.POST['nameRIName'],
		r_quantity = request.POST['nameRQNumber'], 
		r_quantitydescription = request.POST['nameRQDescription'],
		item_status = request.POST['nameRIStatus'],
		date_received = request.POST['nameRIDate'],
		)
	return render(request,'ReceivingSlip.html')

def Feedback(request):
	return render (request, 'Feedback.html')
def createdfeedback(request):
	rcvrfd=ReceiverFeedback.objects.create(
		comments = request.POST['nameComments'],
		Suggestions = request.POST['nameSuggestions'],
		)
	return render(request,'Feedback.html')

def updateDonation(request, pk):

	diane = Donation.objects.get(id=pk)
	form = DonationForm(instance=diane)

	if request.method == 'POST':
		form = DonationForm(request.POST, instance=diane)
		if form.is_valid():
			form.save()
			return redirect('displaydonation')

	context = {'form':form}
	return render(request, 'update.html', context)

def deleteDonation(request, pk):
	diane = Donation.objects.get(id=pk)
	if request.method == "POST":
		diane.delete()
		return redirect('displaydonation')

	context = {'item':diane}
	return render(request, 'delete.html', context)

