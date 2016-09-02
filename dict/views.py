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

        noun = Noun(q)
        noun.fill_the_table()
        normal = Word(q)
        # Word.normalize(normal)
        normal.normalize()
        words = Dictionary.objects.filter(word__exact=normal._normal_word)
        similar_words = {}
        if(len(words) == 0):
            similar_words = Dictionary.objects.filter(word__istartswith=q)
        return render(request, 'dict/search_results.html', {'words': words, 'query': q, 'similar_words': similar_words, 'table_inflection': noun._table})
    return render(request, 'dict/search_form.html', {'error_message': "Please submit the search form!"})
