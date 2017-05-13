import matplotlib.pyplot as plt

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import HttpResponseRedirect

from .forms import NameForm
from .generate_report import report


def index(request):
    return render(request, 'swoosh/index.html')


def get_name(request):
    print "Entering get_name"
    # If this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from request
        form = NameForm(request.POST)
        if form.is_valid():
            your_name = form.cleaned_data['your_name']
            report_data = report(your_name)
            form = NameForm()
            return render(request, 'swoosh/name.html', {
                'form': form,
                'name': your_name,
                'data': report_data
            })
    # If GET or any other method, we'll create a blank form
    else:
        form = NameForm()
    return render(request, 'swoosh/name.html', {'form': form})


def matplot(request):
    return JsonResponse('something', safe=False)
