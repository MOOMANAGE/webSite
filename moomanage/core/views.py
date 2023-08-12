from django.shortcuts import render

# Create your views here.
def frontpage(request):
    return render(request,'core/base.html')
def about(request):
    return render(request,'core/about.html')
def servicios(request):
    return render(request,'core/servicios.html')

def empezar(request):
    return render(request,'core/empezar.html')