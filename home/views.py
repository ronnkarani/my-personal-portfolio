from django.shortcuts import render, HttpResponse
from .models import *
from django.contrib import messages
from django.utils import timezone
from django.core.mail import send_mail

# Create your views here.
def index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'index.html', {'posts': posts})
    # return HttpResponse("this is homepage")
