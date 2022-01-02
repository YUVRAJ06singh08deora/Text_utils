# this file is created by yuvraj singh deora
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    params = {'name': 'Yuvraj', 'place': 'mars'}
    return render(request, 'index.html', params)


def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')
    # check box values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')

    alphacounter = request.POST.get('alphacounter', 'off')
    # checkbox is on
    if removepunc == "on":
        # analysed text
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif (fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to upper case', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n":
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)


    elif (spaceremover == "on"):

        analyzed = ""

        for index, char in enumerate(djtext):

            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

        # Analyze the text

        return render(request, 'analyze.html', params)

    elif (alphacounter == "on"):

        analyzed = len(djtext)

        params = {'purpose': 'length ', 'analyzed_text': analyzed}

        # Analyze the text

        return render(request, 'analyze.html', params)

    else:
        return HttpResponse('Error')
