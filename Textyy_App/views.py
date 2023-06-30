from django.shortcuts import render
from .models import Text

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')


def result(request):
    return render(request, 'result.html')    


#function for textsolver(Actions)

def analyze(request):
    #Input

    text = request.POST.get('textBox','default')
    input_text = text
    #print(text)

    

    #check box value input
    removepunc = request.POST.get('removepunc','Off')
    fullcaps = request.POST.get('fullcaps','Off')
    newlineremover = request.POST.get('newlineremover','Off')
    extraspaceremover = request.POST.get('extraspaceremover','Off')
    fullow = request.POST.get('fullow','Off')

    #print(removepunc)
    
    #logic
    if removepunc == 'on':
      analyzed = ""
      Punctuation = "''!#$%&'()*+,-./:;<=>?@[\]^_`{|}~''"
      
      
      for char in text:
          if char not in Punctuation:
              analyzed = analyzed + char
      text = analyzed

    if fullcaps== 'on':
        analyzed = ""
        for char in text:
            analyzed = analyzed + char.upper()
        text = analyzed
        
    if newlineremover == 'on':
        analyzed = ""
        text = text.replace("\n", "").replace("\r", " ")
        analyzed = text
        text = analyzed

    if fullow == 'on':
        analyzed = ""
        for char in text:
            analyzed = analyzed + char.lower()    
        text = analyzed

    if extraspaceremover == 'on':
        analyzed = ""
        for index, char in enumerate(text):
            if not(text[index] == " " and text[index + 1] == " "):
                analyzed = analyzed + char
       
        text = analyzed

    print(analyzed)

    params = {'analyzed': text}

    #Insert in Database
    model_text = Text(inp_text = input_text, Output_text = text)
    model_text.save() 

    return render(request, 'index.html',params)
