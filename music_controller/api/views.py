from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main(request):
    return HttpResponse("<h1>Hello World!!! NICE :)</h1>")

def test(request):
    return HttpResponse("<h2>This is a test!!!</h2>")