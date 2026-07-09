from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,Http404
from django.shortcuts import redirect,render
from .models import *

menu=[{'title':'About','url_name':'about'},{'title':'Add Post','url_name':'add_page'},{'title':'Contact Us','url_name':'contact'},{'title':'Login','url_name':'login'}]

def index(request):
    posts=Women.objects.all()
    context={
        'title':'Home page',
        'menu':menu,
        'posts':posts
    }
    return render(request,'women/index.html',context=context)

def about(request):
    return render(request,'women/about.html',{'title':'About page','menu':menu})

def addpost(request):
    return HttpResponse('Add post')

def contact(request):
    return HttpResponse('Contact Us')

def login(request):
    return HttpResponse('Login')

def post(request,post_id):
    post=Women.objects.get(id=post_id)

    return HttpResponse(f'<h1>{post.title}</h1><p>{post.content}</p>')


def categories(request,cat):
    if request.GET:
        print(request.GET)
    if cat>10:
        return redirect('home')
    return HttpResponse(f"<h1>States by Categories</h1><p>{cat}</p>")

def pageNotFound(request,exception):
    return HttpResponseNotFound('<h1>Haha Huylo page not found</h1>')