from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

def articles(request):
    return HttpResponse("Hello World!")

def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year=year)
    context = {'year' : year,'article_list' : a_list}
    return render(request, 'news/year_archive.html', context)

def reporter(request, report):
    a_list = Article.objects.filter(reporter=report)
    print('a')
    print(a_list)
    context = {'reporter' : report, 'article_list' : a_list}
    return render(request, 'news/reporter.html',context)

def home(request):
    return render(request,'main/main.html')