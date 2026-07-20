from django.urls import path
from .views import *
urlpatterns=[
    path('',WomenHome.as_view(),name='home'),
    path('cats/<int:cat>/',categories,name='cats'),
    path('about/',about,name='about'),
    path('addpost/',AddPost.as_view(),name='add_page'),
    path('contact/',contact,name='contact'),
    path('login/',login,name='login'),
    path('register/',RegisterUser.as_view(),name='register'),
    path('post/<slug:post_slug>/',ShowPost.as_view(),name='post'),
    path('category/<slug:cat_slug>/',WomenCategory.as_view(),name='category'),
]