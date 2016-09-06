from django.http import HttpResponse
from django.shortcuts import render
from .models import Dictionary
from .magic import Word, Noun


def index(request):
    return HttpResponse("Hello, world.")

def search_form(request):
    return render(request, 'dict/search_form.html')

def search(request):
    if 'q' in request.GET and request.GET['q']:


        q = request.GET['q']
        word = Word(q)
        word.normalize()
        context = {}
        classifier = word._pos

        if(classifier in ['NOUN','NPRO']):
            noun = Noun(q)
            noun.lookup_words()
            context = noun._context

        # normal = Word(q)
        # Word.normalize(normal)

        words = Dictionary.objects.filter(word__exact=word._normal_word)
        similar_words = {}
        if(len(words) == 0):
            similar_words = Dictionary.objects.filter(word__istartswith=q)
        return render(request, 'dict/search_results.html', {'words': words, 'query': q, 'similar_words': similar_words,
                                                            'context': context, 'classifier': classifier})
    return render(request, 'dict/search_form.html', {'error_message': "Please submit the search form!"})
