from django.shortcuts import render

# Create your views here.


def usuario_list(request):
    return render(request, 'inicio.html')
