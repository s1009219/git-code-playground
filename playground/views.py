from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Request -> Response
# Request handler
# Action

def say_hello(request):
    return HttpResponse('Hello World')
    #return render(request, 'hello.html', {'name':'Daniel'})