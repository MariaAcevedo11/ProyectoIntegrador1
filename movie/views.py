from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request): 
    #return HttpResponse('<h1>Hello motherfleckers</h1>')
    #return render(request, 'home.html')
    return render(request, 'home.html', {'name': 'María Acevedo'})
def about(request):
    return HttpResponse('<h1>Welcome to About :D </h1>')
