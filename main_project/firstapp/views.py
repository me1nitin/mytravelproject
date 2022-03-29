from django.shortcuts import render
from django.http import HttpResponse
from .models import places
from .models import team


def index1(request):
    obj1 = places.objects.all()
    obj2 = team.objects.all()
    return render(request, 'index.html', {'result': obj1, 'key2': obj2})
# return HttpResponse('vfghjhvjh')
# Create your views here.
