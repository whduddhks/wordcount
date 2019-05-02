from django.shortcuts import render
import operator
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def count(request):
    full_text = request.GET['fulltext']
    word_list2 = full_text.split('\n')
    word_list = full_text.split()
    word_dictionary={}
    whole=0
    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word] += 1
            whole += len(word)
        else:
            word_dictionary[word] = 1
            whole += len(word)
    sorted_word_dictionary = sorted(word_dictionary.items(), key=operator.itemgetter(1,0), reverse=True)
    return render(request, 'count.html', {"fulltext":word_list2, 'dictionary':sorted_word_dictionary, 'sum':whole})