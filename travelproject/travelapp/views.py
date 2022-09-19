from django.http import HttpResponse
from django.shortcuts import render
from .models import Place
from .models import Person


# Create your views here.

def demo(request, ):
    obj = Place.objects.all()
    obj1 = Person.objects.all()
    return render(request, "index.html", {'result': obj, 'res': obj1})

# def demo(request):
#     obj = Person.objects.all()
#     return render(request, "index.html", {'result': obj})
