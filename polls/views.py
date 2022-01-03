from django.http import HttpResponse
from django.shortcuts import render
from polls.models import Contact

def index(request):
    context ={
        'variable':"this is sent"
    }
    return render(request,'index.html',context)

def aboutus(request):
    return render(request,'about.html')   

def services(request):
    return render(request,'services.html')

def contact(request): 
    if request.method=="POST":
        email=request.POST.get('email')
        name=request.POST.get('name')
        contact=request.POST.get('contact')
        report=request.POST.get('report')
        contact=Contact(email=email, name=name, contact=contact, report=report)
        contact.save()



    return render(request,'contact.html')   
