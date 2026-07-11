from django.urls import path
from .views import *
urlpatterns=[
    path('',index,name='home'),
    path('cats/<int:cat>/',categories,name='cats'),
    path('about/',about,name='about'),
    path('addpost/',addpost,name='add_page'),
    path('contact/',contact,name='contact'),
    path('login/',login,name='login'),
    path('post/<int:post_id>/',post,name='post'),
    path('category/<int:cat_id>/',category,name='category'),
]