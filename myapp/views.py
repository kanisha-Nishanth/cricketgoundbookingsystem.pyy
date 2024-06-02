from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from .forms import registration, LoginForm,ContactForm
from django.core.mail import send_mail
from django.conf import settings

from django.http import HttpResponse

from django.conf import settings

from django.views.generic.base import TemplateView
from django.conf import settings
import stripe
stripe.api_key=settings.STRIPE_SECRET_KEY
def home(request):
    return render(request,'home.html')
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('search')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = registration(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = registration()

    return render(request, 'register.html', {'form': form})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            message=form.cleaned_data['msg']


            send_mail('Greetings from Kanisha',message,settings.EMAIL_HOST_USER,[email])
            return redirect('contact')
    form = ContactForm()
    return render(request,'contact.html',{'form':form})
def search(request):
    return render(request,'search.html')
def about(request):
    return render(request,'about.html')
def ground(request):
    return render(request,'ground.html')

class BookPage(TemplateView):
    template_name = 'book.html'
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['key']=settings.STRIPE_PUBLISHABLE_KEY
        return context
def charge(request):
    if request.method == 'POST':
        def charge(request):
            charge = stripe.charge.create(
                amount=2000,
                currency='inr',
                description='payment gateway',
                source=request.POST['StripeToken']
            )
    return render(request, 'charge.html')

def bookingpage(request):
    return render(request, 'bookingpage.html')


# def send_email(request):
#     if request.method == 'POST':
#         recipient_email = request.POST.get('email')
#         message = request.POST.get('msg')
#
#         subject = 'Your Subject'
#         sender_email = settings.EMAIL_HOST_USER
#
#         send_mail(subject, message, sender_email, [recipient_email])
#         return render(request, 'email_sent.html')
#     return render(request, 'email_form.html')

# def new(request):
#     if request.method == 'POST':
#         form = demoform(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#
#     myform=demoform()
#     return render(request,"new.html",{'form':myform})
# # Create your views here.
