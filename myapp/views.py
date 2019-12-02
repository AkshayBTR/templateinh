from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"Base.html")

def Child1(request):
    return render(request,"Child1.html")

def Child2(request):
    return render(request,"Child2.html")