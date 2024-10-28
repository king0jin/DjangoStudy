from django.shortcuts import render

# Create your views here.
#URL과 요청함수 연결
#프로젝트 urls.py에 작성한 요청시 수행될 함수 작성
 
from django.http import HttpResponse

#1. 기본 요청시, index함수
def index(request):
    # return HttpResponse("kin0jin의 장고 프로젝트~")
    
    #1.1 template - render함수
    return render(request, 'index.html', {'message':"메세지"})
    #클라이언트의 요청, 요청시 출력되는 파일(template), 파일에 전달되는 데이터(키:값)

#2. 문자열 형태의 get 요청시, getItem함수
def getItem(request, itemid):
    #itemid : 넘겨 받은 데이터
    return HttpResponse("<h3>" + itemid + "<h3>")

#2.1 문자열 형태의 get 요청시, 쿼리 적용 queryString함수 
def queryString(request):
    #기본값 설정
    name = request.GET.get("name", "이름 없음")
    return HttpResponse("<h2>" + name + "</h2>")
    #return HttpResponse("<h2>" + request.GET["name"] + "<h2>")
    #queryString/?name=데이터 로 요청 받으면 데이터가 화면에 보인다
  
#3. Post요청시, requestBody함수, formData함수
#ex) 사용자 정보
import json
def requestBody(request):
    user = json.loads(request.body)
    return HttpResponse("이름은 " + user["name"] + "이고 나이는 " + user["age"] + "세이다.")

def formData(request):
    name = request.POST.get("name")
    age = request.POST.get("age")
    return HttpResponse("이름은 " + name + "이고 나이는 " + age + "세이다.")
