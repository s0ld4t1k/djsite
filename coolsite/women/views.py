from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,Http404
from django.shortcuts import redirect,render,get_object_or_404
from .models import *
from .forms import *

menu=[{'title':'About','url_name':'about'},{'title':'Add Post','url_name':'add_page'},{'title':'Contact Us','url_name':'contact'},{'title':'Login','url_name':'login'}]

def index(request):
    posts=Women.objects.all()
    cats=Category.objects.all()
    context={
        'title':'Home page',
        'menu':menu,
        'posts':posts,
        'cats':cats,
        'cat_selected':0
    }
    return render(request,'women/index.html',context=context)

def about(request):
    return render(request,'women/about.html',{'title':'About page','menu':menu})

def addpost(request):
    if request.method=='POST':
        form=AddPostForm(request.POST)
        if form.is_valid():
            try:
                Women.objects.create(**form.cleaned_data)
                return redirect('home')
            except:
                form.add_error(None,'Error adding post')
    else:
        form=AddPostForm()
    context={
        'form':form,
        'menu':menu,
        'title':'Add post'   
    }
    return render(request,'women/addpost.html',context=context)

def contact(request):
    return HttpResponse('Contact Us')

def login(request):
    return HttpResponse('Login')

def post(request,post_slug):
    post=get_object_or_404(Women,slug=post_slug)

    context={
        'post':post,
        'title':post.title,
        'cat_selected':post.cat_id,
        'menu':menu
    }

    return render(request,'women/post.html',context=context)

def category(request,cat_slug):
    cat=get_object_or_404(Category,slug=cat_slug)
    posts=Women.objects.filter(cat_id=cat.id)
    cats=Category.objects.all()

    if len(posts)==0:
        raise Http404()

    context={
        'title':cat.name,
        'menu':menu,
        'posts':posts,
        'cats':cats,
        'cat_selected':cat.id
    }
    return render(request,'women/index.html',context=context)


def categories(request,cat):
    if request.GET:
        print(request.GET)
    if cat>10:
        return redirect('home')
    return HttpResponse(f"<h1>States by Categories</h1><p>{cat}</p>")

def pageNotFound(request,exception):
    return HttpResponseNotFound('<h1>Haha Huylo page not found</h1>')