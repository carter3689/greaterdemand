from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request, 'index.html')

def about_us(request):
    return render(request, 'team.html')

def services(request):
    return render(request, 'service.html')

def contact(request):
    return render(request, 'contact-1.html')
