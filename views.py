from django.http import HttpResponseServerError
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from datetime import date, datetime
from home.models import TechnicalEvent
from home.models import Contact
from home.models import PartiesEvent
from home.models import WeddingEvent
from home.models import CollegeEvent
from home.models import EventAdvisor

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.
from .forms import CreateUserForm
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form=CreateUserForm()
        if request.method == 'POST':
            form=CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user =  form.cleaned_data.get('username')
                messages.success(request, 'Account was created for '+user)

                return redirect('login')

    context={'form':form}
    return render(request,'register.html',context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                    messages.info(request, 'Username OR password is incorrect')

        context={}
        return render(request,'login.html',context)

def logoutUser(request):
	logout(request)
	return redirect('login')



@login_required(login_url='login')
def index(request):
    return render(request,'index.html')

@login_required(login_url='login')
def about(request):
    return render(request,'about.html')

@login_required(login_url='login')
def payment(request):
    return render(request,'payment.html')

@login_required(login_url='login')
def confirm(request):
    return render(request,'confirm.html')

@login_required(login_url='login')
def technicalevent(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        destination = request.POST.get('destination')
        date =  request.POST.get('date')
        time =  request.POST.get('time')
        guest =  request.POST.get('guest')
        technicalevent = EventAdvisor(name=name, email=email, phone=phone, destination=destination,date = date,time = time,guest = guest, desc =desc)
        technicalevent.save()
        return render(request,'payment.html')
    return render(request,'technicalevent.html')


@login_required(login_url='login')
def partiesevent(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        destination = request.POST.get('destination')
        date =  request.POST.get('date')
        time =  request.POST.get('time')
        guest =  request.POST.get('guest')
        partiesevent = PartiesEvent(name=name, email=email, phone=phone, destination=destination,date = date,time = time,guest = guest, desc =desc)
        partiesevent.save()
        return render(request,'payment.html')
   
    return render(request,'partiesevent.html')

@login_required(login_url='login')
def collegeevent(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        destination = request.POST.get('destination')
        date =  request.POST.get('date')
        time =  request.POST.get('time')
        guest =  request.POST.get('guest')
        collegeevent = CollegeEvent(name=name, email=email, phone=phone, destination=destination,date = date,time = time,guest = guest, desc =desc)
        collegeevent.save()
        return render(request,'payment.html')

    return render(request,'collegeevent.html')

@login_required(login_url='login')
def eventadvisor(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        destination = request.POST.get('destination')
        date =  request.POST.get('date')
        time =  request.POST.get('time')
        guest =  request.POST.get('guest')
        eventadvisor = EventAdvisor(name=name, email=email, phone=phone, destination=destination,date = date,time = time,guest = guest, desc =desc)
        eventadvisor.save()
        return render(request,'payment.html')
    return render(request,'eventadvisor.html')

@login_required(login_url='login')
def weddingevent(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        destination = request.POST.get('destination')
        date =  request.POST.get('date')
        time =  request.POST.get('time')
        guest =  request.POST.get('guest')
        weddingevent = WeddingEvent(name=name, email=email, phone=phone, destination=destination,date = date,time = time,guest = guest, desc =desc)
        weddingevent.save()
        
        return render(request,'payment.html')
            
    return render(request,'weddingevent.html')



@login_required(login_url='login')
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')
