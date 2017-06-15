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
    else:
        form = NameForm()
    return render(request, 'swoosh/name.html', {'form': form})


def matplot(request):
    global json_data
    if json_data is None:
        status = 1
    else:
        status = 0
    return JsonResponse({'json_data': json_data, 'status': status}, safe=False)
