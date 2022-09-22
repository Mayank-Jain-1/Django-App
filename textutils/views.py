from string import punctuation
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
  return render(request, 'index.html')
  
def analyze(request):
  djText = request.GET.get('text', 'nothing')
  
  analyzedText = ''
  punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
  for i in djText:
    if i not in punctuation:
      analyzedText += i

  params = {'analyzedText':analyzedText}
  return render(request, 'analyze.html', params)
  