from django.shortcuts import render, HttpResponse
from .models import *
from django.contrib import messages
from django.utils import timezone
from django.core.mail import send_mail

# Create your views here.
def index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        msg = request.POST.get('msg')
        
        #send Email
        send_mail(
            #subject
            'New Message from ' + name,
            #message
            msg,
            #from Email
            email,
            #to Email
            ['karanironny25@gmail.com'],
        )
        
        messages.success(request, 'Your message has been sent!')
        return render(request, 'index.html', {'name': name})
    else:
        return render(request, 'index.html', {'posts': posts})
    # return HttpResponse("this is homepage")
