from django.http import HttpResponse
from django.shortcuts import render
from .forms import ZapisForm, BackForm


def index(request):
    return render(request, 'index.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = ZapisForm(request.POST)
        form1 = BackForm(request.POST)
        if form.is_valid():
            form.save()
        elif form1.is_valid():
            form1.save()
        else:
            error = 'Заполните обязательные поля!'
    form = ZapisForm()
    form1 = BackForm()
    data = {
        'form': form,
        'form1': form1,
        'error': error
    }
    return render(request, 'index.html', data)




