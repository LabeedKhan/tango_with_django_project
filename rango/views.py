from django.shortcuts import render
# create simple view
# send text to client 
from django.http import HttpResponse

def index(request):
    context_dict= {'boldmessage': "Crunchy,creamy,cookie,candy,cupcake!"}
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return HttpResponse("<a href='/rango/about/'>About</a><a href= /rango/>Index</a> "  )