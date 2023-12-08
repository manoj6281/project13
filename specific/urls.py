from specific.views import *
from django.urls import path

app_name='thinking'

urlpatterns=[
    path('brahma/',brahma,name='brahma'),
    path('bhuvi/',bhuvi,name='bhuvi'),
]