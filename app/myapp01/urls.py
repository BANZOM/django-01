from django.urls import path
from . import views

urlpatterns = [ 
    path('function/', views.hello_world, name='hello_world'),
    path('function2/', views.hello_world2, name='hello_world2'),
    path('class/', views.HelloWorldView.as_view(), name='class_hello_world'),
]