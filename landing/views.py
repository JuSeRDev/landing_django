from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
def home(request):
  return render(request,'landing/index.html')

def diploma(request):
  return render(request, 'landing/diploma.html')

def gestor(request):
  return render(request, 'landing/gestor.html')