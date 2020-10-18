from django.shortcuts import render, redirect
from .models import direct
from .forms import directForm
import os


def main(request):
    return render(request, 'main/main.html')


def add(request):
    error = ''
    if request.method == 'POST':
        form = directForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main')
        else:
            error = 'Фома была некорректной'

    form = directForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/add.html', context)


def data(request):
    files = direct.objects.all()
    extensions = []
    for el in files:
        extensions.append(os.path.splitext(el.samFile.path)[1][1:])
    fusion = zip(files, extensions)
    return render(request, 'main/data.html', {'title': 'Файлы директории',
                                              'fusion': fusion,
                                              })
