from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'example/homePage.html')

def glav(request):
    return render(request, 'example/glav.html', {'values': ['Это главная страница, чтобы убедиться, что все окес']})

def foto(request):
    return render(request, 'example/dddd.html')
