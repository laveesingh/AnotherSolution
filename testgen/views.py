# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .forms import CaseForm

# Create your views here.


def get_tests(request):
    if request.method == 'POST':
        # Do something that happens after post
        pass
    else:
        form = CaseForm()
    return render(request, 'testgen/welcome.html', {'form': form})
