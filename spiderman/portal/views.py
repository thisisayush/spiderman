# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request, 'portal/index.html')

@login_required
def manage(request):
    return render(request, 'portal/admin/index.html')