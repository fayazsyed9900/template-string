from django.urls import path
from app2.views import *

app_name='something2'

urlpatterns=[

    path('string3/',string3,name='string3'),
    
    path('string4/',string4,name='string4'),
]