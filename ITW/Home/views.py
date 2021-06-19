from django.shortcuts import render, HttpResponse
from datetime import datetime
from Home.models import Contact
from django.contrib import messages
from Home.models import Contactus

def index(request):
    return render(request, 'index.html')
def contactus(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contactus = Contactus(name=name, email=email, message=message, date= datetime.today())
        contactus.save()
        messages.success(request, 'Message has been sent.')
    return render(request, 'contactus.html')
def about(request):
    return render(request, 'about.html')
def alerts(request):
    return render(request, 'alerts.html')
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        qualification = request.POST.get('qualification')
        intro = request.POST.get('intro')
        last_name = request.POST.get('last_name')
        contact = Contact(name=name, email=email,phone=phone, last_name=last_name,qualification = qualification ,intro =intro)
        contact.save()
        messages.success(request, 'Profile details updated.')
    return render(request, 'contact.html')
def base(request):
    return render(request, 'base.html')


# Create your views here.
