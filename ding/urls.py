
from django.urls import path

from . import login

urlpatterns = [

    path('ding_url/', login.ding_url),
    path('ding_back/', login.ding_back),

]