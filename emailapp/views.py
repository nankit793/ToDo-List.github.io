from django.conf import settings
from django.shortcuts import render
from django.core.mail import send_mail
  
def index(request):
    return render(request, 'index.html')


def about(request): 
    email = request.POST.get('textfield')
    name  = request.POST.get('namefield')
    subject = 'Test Mail'
    message = 'thank you for registring to our site'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email] 
    send_mail( subject, message, email_from, recipient_list )
    params = {'emailname': email, 'name': name }
    return render(request, 'about.html', params)    
     
  