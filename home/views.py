from django.shortcuts import render

def home_page(request):
    return render(request, 'home.html')

def about_page(request):
    return render(request, 'about.html')

def contact_page(request):
    return render(request, 'contact.html')

def project_page(request):
    return render(request, 'project.html')

