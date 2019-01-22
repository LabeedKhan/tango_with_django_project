from django.shortcuts import render
# create simple view
# send text to client 
from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says Hello")

def index(request):
    context_dict= {'boldmessage': "Crunchy, creamy, cookie"}
    return render(request, 'rango/index.html', context=context_dict)

