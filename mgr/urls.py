from django.urls import path

from mgr import devices

urlpatterns = [

    path('devices', devices.dispatcher),

]