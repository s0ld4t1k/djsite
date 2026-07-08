from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,Http404
from django.shortcuts import redirect,render
from .models import *

menu=['About','Add Post','Contact Us','Login']

def index(request):
    posts=Women.objects.all()
    return render(request,'women/index.html',{'title':'Home page','menu':menu,'posts':posts})

def about(request):
    return render(request,'women/about.html',{'title':'About page','menu':menu})

def categories(request,cat):
    if request.GET:
        print(request.GET)
    if cat>10:
        return redirect('home')
    return HttpResponse(f"<h1>States by Categories</h1><p>{cat}</p>")

def pageNotFound(request,exception):
    return HttpResponseNotFound('<h1>Haha Huylo page not found</h1>')