from . import views
from django.urls import path
from django.urls import include 

urlpatterns = [
    path('post/<slug:slug>',views.post_page,name='post_page')
]