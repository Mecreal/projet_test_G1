from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
# Create your views here.

name = 'G1'
class Home(View):
    def get(self, request):
        return render(request,'hello.html',{'m':name})