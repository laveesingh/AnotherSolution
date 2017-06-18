# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse

from .forms import CaseForm
from . import utils


def get_tests(request):
    form = CaseForm()
    return render(request, "testgen/welcome.html", {"form": form})


def generate_case(request):
    request_data = {}
    print "Got ajax request with data:"
    for s in request.POST:
        request_data[s] = str(request.POST[s])
        print s, ":", request_data[s], type(request_data[s])
    if request_data["include_tests"] == "true":
        content = request_data["no_of_tests"]
        for i in xrange(int(request_data["no_of_tests"])):
            content += "<br />"
            content += utils.generate_case_util(request_data)
    else:
        content = utils.generate_case_util(request_data)
    print "Serving content to ajax request:", content
    return JsonResponse({"content": content})