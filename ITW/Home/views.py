from django.shortcuts import render, HttpResponse
def index(request):
    return render(request, 'index.html')
def contact(request):
    return render(request, 'contact.html')
def about(request):
    return render(request, 'about.html')
def faq(request):
    return render(request, 'faq.html')
def alerts(request):
    return render(request, 'alerts.html')
def apply(request):
    return render(request, 'apply.html')
def base(request):
    return render(request, 'base.html')

