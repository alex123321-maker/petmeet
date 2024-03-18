from .views import *
from django.urls import path

urlpatterns = [
    path( 'register', CreateUserView.as_view(), name='register'),
    path('example/', ExampleView.as_view(), name='example'),
]