from django.http import HttpResponse
from django.shortcuts import render



def index(request):
  return render(request, 'index.html')

def removePunc(request):
  return HttpResponse('<h1>Remove punc</h1><a href = "http://localhost:8000">sdfsdaf</a>')
  
def capFirst(request):
  return HttpResponse('<h1>capfirst</h1>')
  
def removeSpace(request):
  return HttpResponse('<h1>remove space</h1>')
  