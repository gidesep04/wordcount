from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):
    return render(request,'home.html',{'intro':'Welcome to my first django website','task':'Word Count'})


def count(request):
    fulltext= request.GET['fulltext']
    wordlist=fulltext.split()

    wordDictionary={}

    for word in wordlist:
        if word in wordDictionary:
            #increase
            wordDictionary[word]+=1
        else:
            #add to the dictionary
            wordDictionary[word] = 1

    sortedWords=sorted(wordDictionary.items(),key= operator.itemgetter(1),reverse=True)

    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),'sortedWords':sortedWords})


def kids(request):
    return HttpResponse('<h1>Kids make home sweet</h1>')