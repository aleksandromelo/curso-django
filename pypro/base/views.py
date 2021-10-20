from django.http import HttpResponse
# from django.shortcuts import render, redirect

# Create your views here.


def home(request):
    return HttpResponse('<html><body>Olá, Django!</body></html>', content_type='text/html')
