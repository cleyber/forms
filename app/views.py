from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import User

def index(request):
    if request.method == 'POST':
        form = IndexForm(request.)
        user = User()
        user.name = request.POST.get('name')
        user.last_name = request.POST.get('last_name')
        user.save()
        return render(request, 'app/response.html')

    return render(request, 'app/index.html')


def response(request):
    list = User.objects.all()
    context = {'list': list,}
    return render(request, 'app/response.html', context)
