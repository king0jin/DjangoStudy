from django.shortcuts import render

# Create your views here.
#URL과 요청함수 연결
#프로젝트 urls.py에 작성한 요청시 수행될 함수 작성
 
from django.http import HttpResponse

#1. 기본 요청시, index함수
def index(request):
    return HttpResponse("kin0jin의 장고 프로젝트~")

