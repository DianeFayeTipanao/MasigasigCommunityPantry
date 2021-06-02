from django.shortcuts import redirect, render
from CommunityPantry.models import ReceiverInfo, ReceivedDonations

#Displaying ReceiverInformation
def receiver_info(request):
	return render(request,'ReceiverSlip.html')
	views_RInfo = ReceiverInfo.objects.all()
	return render(request, 'ReceiverSlip.html', {'ReceiverInfo': views_RInfo})

#Displaying ReceivedDonations
def received_donation(request, rd_id):
	views_RDonation = ReceivedDonations.objects.get(id=rd_id)
	ReceivedDonations.objects.create(item_received=request.POST['nameIReceived'], r_quantity=request.POST['nameRQuantinty'], r_quantitydescription=request.POST['nameRQDescription'], item_status=request.POST['nameIStatus'], date_received=request.POST['nameDReceived'], ReceivedDonations=views_RDonation)
	return render(request, 'ReceivingSlip.html', {'received_id': views_RDonation})

#Displaying ReceiverInfo in ReceivingSlip.html
def add_RInfo(request):
	new_info = ReceiverInfo.objects.create(r_name=request.POST['nameRName'], r_contact=request.POST['nameRContact'], r_address=request.POST['nameRAddress'], r_affiliation=request.POST['nameRAffiliation'])
	return redirect (f'/CommunityPantry/{new_info.id}/')

#Displaying ReceivedDonations in different URL
def new_RDonation(request, ri_id):
	add_rdonations = ReceivedDonations.object.get(id=ri_id)
	ReceivedDonations.objects.create(item_received=request.POST['nameIReceived'], r_quantity=request.POST['nameRQuantinty'], r_quantitydescription=request.POST['nameRQDescription'], item_status=request.POST['nameIStatus'], date_received=request.POST['nameDReceived'], ReceivedDonations=add_rdonations)
	return redirect (f'/CommunityPantry/{add_rdonations.id}/')

'''def receiver_feedback(request, rf_id):
	return render(request,'RFeedbackForm.html')
	views_RFeedback = ReceiverInfo.object.get(id=rf_id)
	return render(request,'RFeedbackForm.html', {ReceiverInfo: views_RFeedback})

def donator_info(request):
	return render(request,'DInfoForm.html')
	views_DInfo = DonatorInfo.objects.all()
	return render(request,'DInforForm.html', {'DInventory': views_DInfo})

def donation_inventory(request,di_id):
	views_DInventory = DonatorInfo.objects.get(id=di_id)
	return render(request,'DInventoryForm.html', {'DonatorInfo': views_DInventory})

def donation_status(request,ds_id):
	views_DStatus = DInventory.objects.get(id=ds_id)
	return render (request,'DStatusForm.html',{'DInventory': views_DStatus})'''

# Create your views here.
