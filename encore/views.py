from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(req):
    return HttpResponse("엔코아에 오신 것을 환영합니다.")