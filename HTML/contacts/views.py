from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .models import Contact

# Create your views here.

def contact(request):
    if request.method =='POST':
        service_id = request.POST['service_id']
        service = request.POST['service']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        
        contact = Contact(service=service, service_id=service_id, name=name, email=email, phone=phone, message=message, user_id=user_id)

        contact.save()

        #send email
        send_mail(
               'Contact Inquery',
                'there has been an inquiry for ' + service + '. Sign into admin panel for more info',
                'jon.richcreek@gmail.com',
                ['jon.richcreek@gmail.com'],
                fail_silently=False
        )

        messages.success(request, 'Your message has been submitted, We will get back to you as soon as possible.')
        return redirect('index')
        