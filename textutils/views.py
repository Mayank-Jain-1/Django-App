from ast import AnnAssign
from string import punctuation
from django.http import HttpResponse
from django.shortcuts import render
import re


def index(request):
  return render(request, 'index.html')
  
def analyze(request):
  
  punctuations = r'''=!()-[]{};:'"\,<>/?@#$%^&*_~'''
  
  
  djText = request.POST.get('text', 'Please enter some text to analyze...')
  removePunc = request.POST.get('removePunc', 'off')
  capFirst = request.POST.get('capFirst', 'off')
  removeSpace = request.POST.get('removeSpace', 'off')
  removeNewLines = request.POST.get('removeNewLines', 'off')
  
  analyzedText = djText


  if removePunc == 'on':
    temp = ''
    for i in analyzedText:
      if i not in punctuations or i == ' ':
        temp += i
    analyzedText = temp

  if removeNewLines == 'on':
    temp = analyzedText.split('\r')
    temp = ''.join([x.replace('\n','') for x in temp])
    analyzedText = temp

  if removeSpace == 'on':
    analyzedText = re.sub(' +', ' ', analyzedText) 
  
  if capFirst == 'on':
    sentences = analyzedText.split('.')
    analyzedText = ". ".join(map(lambda x : x.strip().capitalize(), sentences))
  

  params = {'analyzedText':analyzedText,
            'removePunc': removePunc,
            'capFirst': capFirst,
            'removeSpace': removeSpace
  }
  return render(request, 'analyze.html', params)
  