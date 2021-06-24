from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeBase),
    path('Homepage', views.HomeBase, name="Homepage"),
    path('Feedback', views.Feedback, name="Feedback"),

    path('donator', views.donator, name="donator"),
    path('createdonator', views.createdonator, name="createdonator"),
    path('createddonation', views.createddonation, name="createddonation"),
    path('displaydonation', views.displaydonation, name="displaydonation"),

    path('receiver', views.receiver, name="receiver"),
    path('createdreceiver', views.createdreceiver, name="createdreceiver"), 
    path('createdreceived', views.createdreceived, name="createdreceived"), 

    path('Feedback', views.Feedback, name="Feedback"),
    path('createdfeedback', views.createdfeedback, name="createdfeedback"),

    path('update_donation/<str:pk>/', views.updateDonation, name="update_donation"),
    path('delete_donation/<str:pk>/', views.deleteDonation, name="delete_donation"),

    #path('donatorform', views.donatorform, name="donatorform"),
    #path('receiverform', views.receiverform, name="receiverform"),
]