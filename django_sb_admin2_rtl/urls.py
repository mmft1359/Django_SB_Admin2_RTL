from django.conf.urls import url
from django_sb_admin2_rtl.views import *

urlpatterns = [
    url(r'^$', dashboard, name='dashboard'),
    url(r'^index/$', dashboard, name='dashboard'),
    url(r'^flot/$', flot, name='flot'),
    url(r'^morris/$', morris, name='morris'),
    url(r'^tables/$', tables, name='tables'),
    url(r'^forms/$', forms, name='forms'),
    url(r'^panels-wells/$', panels_wells, name='panels_wells'),
    url(r'^buttons/$', buttons, name='buttons'),
    url(r'^notifications/$', notifications, name='notifications'),
    url(r'^typography/$', typography, name='typography'),
    url(r'^grid/$', grid, name='grid'),
    url(r'^blank/$', blank, name='blank'),
    url(r'^login/$', login, name='login'),
]
