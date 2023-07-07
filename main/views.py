from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def result(request):
    return render(request, 'result.html')

def ESJ(request):
    return render(request, 'esj.html')
def ESP(request):
    return render(request, 'esp.html')
def ENJ(request):
    return render(request, 'enj.html')
def ENP(request):
    return render(request, 'enp.html')
def ISJ(request):
    return render(request, 'isj.html')
def ISP(request):
    return render(request, 'isp.html')
def INJ(request):
    return render(request, 'inj.html')
def INP(request):
    return render(request, 'inp.html')