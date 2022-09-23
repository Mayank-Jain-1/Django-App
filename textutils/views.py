from ast import AnnAssign
from string import punctuation
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
  return render(request, 'index.html')
  
def analyze(request):
  
  punctuations = '''!()-[]{};:'"\,<>/?@#$%^&*_~'''
  
  
  djText = request.GET.get('text', 'nothing')
  analyzedText = djText

  removePunc = request.GET.get('removePunc', 'off')
  capFirst = request.GET.get('capFirst', 'off')
  removeSpace = request.GET.get('removeSpace', 'off')

  if removePunc == 'on':
    temp = ''
    for i in analyzedText:
      if i not in punctuations or i == ' ':
        temp += i
    analyzedText = temp
  if capFirst == 'on':
    sentences = analyzedText.split('.')
    print(sentences)
    analyzedText = ". ".join(map(lambda x : x.strip().capitalize(), sentences))


  params = {'analyzedText':analyzedText,
            'removePunc': removePunc,
            'capFirst': capFirst,
            'removeSpace': removeSpace
  }
  return render(request, 'analyze.html', params)
  