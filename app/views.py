from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

from .models import User
from .forms import IndexForm

def index(request):
    if request.method == 'POST':
        form = IndexForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app:response')
    else:
        form = IndexForm()

    return render(request, 'app/index.html', {'form': form})


def response(request):
    list = User.objects.all()
    context = {'list': list,}
    return render(request, 'app/response.html', context)
