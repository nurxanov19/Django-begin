from django.shortcuts import render
from django.http import HttpResponse

def describe_options(request):
    return HttpResponse('Our AI assistance has 3 versions: Community (free)  |  Plus (20/per month)  | Pro (200/per month)')

def pro(request):
    return HttpResponse('It is the best model for all intensive tasks. Chose payment option, [insert your card]')

def plus(request):
    return HttpResponse('This model is best for daily tasks. To activate, insert your card and choose tariff')
