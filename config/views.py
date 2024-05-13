from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(req):
    return HttpResponse("여기는 장고 메인!!!")