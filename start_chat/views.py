from django.shortcuts import render
from django.http import HttpResponse

def start(request):
    return HttpResponse('Type anything you need help on')

def history(request):
    return HttpResponse("You didn't even tried on chatting")
