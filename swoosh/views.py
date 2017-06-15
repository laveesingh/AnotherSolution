import matplotlib.pyplot as plt

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import HttpResponseRedirect

from .forms import NameForm
from .generate_report import report


def index(request):
    return render(request, 'swoosh/index.html')

json_data = None
def get_name(request):
    global json_data
    json_data = None
    if request.method == 'POST':
        # create a form instance and populate it with data from request
        form = NameForm(request.POST)
        if form.is_valid():
            your_name = form.cleaned_data['your_name']
            report_data = report(your_name)
            json_data = report_data
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
    global json_data
    if json_data is None:
        print "Json_data isn't being set"
        status = 1
    else:
        print "Json_data is being set"
        status = 0
    for s in json_data:
        print s, json_data[s], type(json_data[s])
    return JsonResponse({'json_data': json_data, 'status': status}, safe=False)
