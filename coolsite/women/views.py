from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,Http404
from django.shortcuts import redirect,render,get_object_or_404
from .models import *
from .forms import *
from .utils import *
from django.views.generic import ListView,DetailView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.urls import reverse_lazy


class WomenHome(DataMixin,ListView):
    model=Women
    template_name='women/index.html'
    context_object_name='posts'

    def get_context_data(self,*,object_list=None,**kwargs):
        context=super().get_context_data(**kwargs)
        c_def=self.get_user_context(title='Home Page')
        return dict(list(context.items())+list(c_def.items()))

    def get_queryset(self):
        return Women.objects.filter(is_published=True)

class WomenCategory(DataMixin,ListView):
    model=Women
    template_name='women/index.html'
    context_object_name='posts'
    allow_empty=False

    def get_context_data(self,*,object_list=None,**kwargs):
        context=super().get_context_data(**kwargs)
        c_def=self.get_user_context(title=context['posts'][0].cat,cat_selected=context['posts'][0].cat_id)
        return dict(list(context.items())+list(c_def.items()))

    def get_queryset(self):
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'],is_published=True)

class ShowPost(DataMixin,DetailView):
    model=Women
    template_name='women/post.html'
    slug_url_kwarg='post_slug'
    context_object_name='post'

    def get_context_data(self,*,object_list=None,**kwargs):
        context=super().get_context_data(**kwargs)
        c_def=self.get_user_context(title=context['post'])
        return dict(list(context.items())+list(c_def.items()))

class AddPost(LoginRequiredMixin,DataMixin,CreateView):
    form_class=AddPostForm
    template_name='women/addpost.html'
    login_url='/admin/'
    raise_exception=True

    def get_context_data(self,*,object_list=None,**kwargs):
        context=super().get_context_data(**kwargs)
        c_def=self.get_user_context(title='Add Post')
        return dict(list(context.items())+list(c_def.items()))
    

# def index(request):
#     posts=Women.objects.all()
#     cats=Category.objects.all()
#     context={
#         'title':'Home page',
#         'menu':menu,
#         'posts':posts,
#         'cats':cats,
#         'cat_selected':0
#     }
#     return render(request,'women/index.html',context=context)

def about(request):
    contact_list=Women.objects.all()
    paginator=Paginator(contact_list,3)

    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)

    return render(request,'women/about.html',{'page_obj':page_obj,'title':'About page','menu':menu})

# def addpost(request):
#     if request.method=='POST':
#         form=AddPostForm(request.POST)
#         if form.is_valid():
#             try:
#                 Women.objects.create(**form.cleaned_data)
#                 return redirect('home')
#             except:
#                 form.add_error(None,'Error adding post')
#     else:
#         form=AddPostForm()
#     context={
#         'form':form,
#         'menu':menu,
#         'title':'Add post'   
#     }
#     return render(request,'women/addpost.html',context=context)

def contact(request):
    return HttpResponse('Contact Us')

def login(request):
    return HttpResponse('Login')

class RegisterUser(DataMixin,CreateView):
    form_class=RegisterUserForm
    template_name='women/register.html'
    success_url=reverse_lazy('login')

    def get_context_data(self,*,object_list=None,**kwargs):
        context=super().get_context_data(**kwargs)
        c_def=self.get_user_context(title='Register')
        return dict(list(context.items())+list(c_def.items()))


# def post(request,post_slug):
#     post=get_object_or_404(Women,slug=post_slug)

#     context={
#         'post':post,
#         'title':post.title,
#         'cat_selected':post.cat_id,
#         'menu':menu
#     }

#     return render(request,'women/post.html',context=context)

# def category(request,cat_slug):
#     cat=get_object_or_404(Category,slug=cat_slug)
#     posts=Women.objects.filter(cat_id=cat.id)
#     cats=Category.objects.all()

#     if len(posts)==0:
#         raise Http404()

#     context={
#         'title':cat.name,
#         'menu':menu,
#         'posts':posts,
#         'cats':cats,
#         'cat_selected':cat.id
#     }
#     return render(request,'women/index.html',context=context)


def categories(request,cat):
    if request.GET:
        print(request.GET)
    if cat>10:
        return redirect('home')
    return HttpResponse(f"<h1>States by Categories</h1><p>{cat}</p>")

def pageNotFound(request,exception):
    return HttpResponseNotFound('<h1>Haha Huylo page not found</h1>')