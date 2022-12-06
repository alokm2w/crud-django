from django.shortcuts import render, HttpResponse
from Home.models import Contact
from datetime import datetime
from django.contrib import messages
from .forms import ContactUs

# Create your views here.
def index(request):
    context={
        'pageName':'Home'
    }
    return render(request, 'index.html', context)
    # return HttpResponse('This is Home page')

def about(request):
    context={
        'pageName':'About'
    }
    return render(request, 'about.html', context)

def services(request):
    context={
        'pageName':'Services'
    }
    return render(request, 'services.html', context)

def contact(request):

    # use for print
    # return HttpResponse(str(var))

    if request.method == 'POST':
        contacts = ContactUs(request.POST)
    else:
        contacts = ContactUs()
        return render(request, 'contact.html', {'quesries':contacts})

        # name = request.POST.get('name')
        # email =request.POST.get('email')
        # phone =request.POST.get('phone')
        # message =request.POST.get('message')

        # contact = Contact(name=name, email=email, phone=phone, message=message, date=datetime.today())
        # contact.save()
    # context={
    #     'pageName':'Contact Us'
    # }
    # messages.success(request, "Submitted successfully!" )
    # return render(request, 'contact.html', context)

def update(request):
    context={
        'pageName':'Services'
    }
    return render(request, 'update.html', context)

def show(request):
    context={
        'pageName':'Services'
    }
    return render(request, 'show.html', context)
    