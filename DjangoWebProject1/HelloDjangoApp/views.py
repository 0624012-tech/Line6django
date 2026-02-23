from django.shortcuts import render
from django.http import HttpResponse 
from datetime import datetime 

# Create your views here.
def index(request):
    now = datetime.now()

    return render(
        request,
        "HelloDjangoApp/index.html", 
        { 
            'title' : "Django home",
            'message' : "hello Django",
            'content' : "on" + now.strftime("%A, %d %B, %Y at %X")
        }
 ) 
   