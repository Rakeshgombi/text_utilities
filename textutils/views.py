from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcase', 'off')
    smallcaps = request.POST.get('smallcase', 'off')
    newline = request.POST.get('newline', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    analyzed = ""

    if removepunc == "on":
        punctuations = """.,;:?!-()[]{}"'/@&-*^%<>#_$+="""
        for char in djtext:
            if char not in punctuations:
                analyzed += char
        params = {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if fullcaps == "on":
        analyzed = ""
        analyzed += djtext.upper()
        params = {'purpose': 'UPPER CASE', 'analyzed_text': analyzed}
        djtext = analyzed

    if smallcaps == "on":
        analyzed = ""
        analyzed += djtext.lower()
        params = {'purpose': 'SMALL CASE', 'analyzed_text': analyzed}
        djtext = analyzed

    if newline == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed += char
        params = {'purpose': 'New Line Remover', 'analyzed_text': analyzed}
        djtext = analyzed

    if extraspaceremover == 'on':
        analyzed = ""
        for i, char in enumerate(djtext):
            if not (djtext[i] == " " and djtext[i + 1]) == " ":
                analyzed += char
        params = {'purpose': 'Remove Extra Spaces', 'analyzed_text': analyzed}
        djtext = analyzed

    if charcount == 'on':
        analyzed = ""
        analyzed = len(djtext)
        params = {'purpose': 'Count Character',
                  'analyzed_text': f"Number of characters in the Textbox is: {analyzed}"}
        djtext = analyzed

    if removepunc != "on" and charcount != 'on' and extraspaceremover != 'on' and newline != "on" and \
            smallcaps != "on" and fullcaps != "on":
        return HttpResponse("SORRY PLEASE SELECT ANY OPTION")

    return render(request, 'analyze.html', params)
