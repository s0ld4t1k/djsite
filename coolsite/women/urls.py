from django.urls import path
from .views import *
urlpatterns=[
    path('',index,name='home'),
    path('cats/<int:cat>/',categories,name='cats'),
    path('about/',about,name='about'),
    path('addpost/',addpost,name='add_page'),
    path('contact/',contact,name='contact'),
    path('login/',login,name='login'),
    path('post/<slug:post_slug>/',post,name='post'),
    path('category/<slug:cat_slug>/',category,name='category'),
]