# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def dashboard(request):
    return render(request, "django_sb_admin2_rtl/index.html")


def index(request):
    dashboard(request)


def flot(request):
    return render(request, "django_sb_admin2_rtl/flot.html")


def morris(request):
    return render(request, "django_sb_admin2_rtl/morris.html")


def tables(request):
    return render(request, "django_sb_admin2_rtl/tables.html")


def forms(request):
    return render(request, "django_sb_admin2_rtl/forms.html")


def panels_wells(request):
    return render(request, "django_sb_admin2_rtl/panels-wells.html")


def buttons(request):
    return render(request, "django_sb_admin2_rtl/buttons.html")


def notifications(request):
    return render(request, "django_sb_admin2_rtl/notifications.html")


def typography(request):
    return render(request, "django_sb_admin2_rtl/typography.html")


def grid(request):
    return render(request, "django_sb_admin2_rtl/grid.html")


def blank(request):
    return render(request, "django_sb_admin2_rtl/blank.html")


def login(request):
    return render(request, "django_sb_admin2_rtl/login.html")
