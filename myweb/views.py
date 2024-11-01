from django.shortcuts import render, get_object_or_404

# Create your views here.
#URL과 요청함수 연결
#프로젝트 urls.py에 작성한 요청시 수행될 함수 작성
 
from django.http import HttpResponse, JsonResponse

#CRUD작업 - 사용하고 싶은 테이블(모델) 불어오기
from myweb.models import Item
#CURD작업 - 특정 필드의 최대값을 가져오기 위해 사용
from django.db.models import Max
#CRUD작업 - HTTP 요청을 처리하는 도중에 특정 URL로 사용자를 리디렉션하기 위해 사용
from django.shortcuts import redirect
#CURD작업 - JSON데이터 처리를 위해 사용
import json

#1. 기본 요청시, index함수
#6. CRUD - 기본 요청시, 테이블 모든 데이터 조회
def index(request):
    # return HttpResponse("kin0jin의 장고 프로젝트~")
    #1.1 template - render함수
    # return render(request, 'index.html', {'message':"메세지"})
    #클라이언트의 요청, 요청시 출력되는 파일(template), 파일에 전달되는 데이터(키:값)

    #6. 전체 조회를 데이터 모두 가져오기
    data = Item.objects.all()
    print(data)
    return render(request, 'index.html', {'data':data})

#7. CURD - 상품ID값 형태로의 해당 상품 정보 요청시, detail함수
def detail(request, itemid):
    item = get_object_or_404(Item, itemid=itemid)
    print(item)
    return render(request, 'index_detail.html', {'item': item})

#8. CURD - insert요청시, insert함수
#8.1 CRUD - 데이터 수정
def insert(request):
    if request.method == "POST":
        item = Item()
        data = json.loads(request.body)
        itemid = data.get("itemid")
        if itemid:
            # 데이터 수정 - itemid로 기존 아이템 가져오기
            try:
                item = Item.objects.get(itemid=itemid)
            except Item.DoesNotExist:
                return JsonResponse({"error": "Item not found"}, status=404)
        else:
            # 데이터 삽입 - 최대 itemid 계산
            obj = Item.objects.aggregate(itemid=Max("itemid"))
            if obj['itemid'] is None:
                obj['itemid'] = 0
            item.itemid = int(obj['itemid']) + 1

        item.itemname = data.get("itemname", "이름없음")
        item.description = data.get("description", "설명없음")
        item.price = data.get("price", 0)
        item.pictureurl = data.get("pictureurl", "이미지없음")
        item.save()
        #시작 페이지로 리다이렉트
        return redirect('/')
    #8.2 CRUD - 데이터 삭제
    elif request.method == "DELETE":
        item = Item()
        data = json.loads(request.body)
        itemid = data.get("itemid")
        if itemid:
            try:
                item = Item.objects.get(itemid=itemid)
                item.delete()
                item.save()
            except Item.DoesNotExist:
                return JsonResponse({"error": "Item not found"}, status=404)

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

#4. fileupload요청시, fileUpload함수
from django.core.files.storage import FileSystemStorage
import uuid
def fileUpload(request):
    #4.1 file이라는 이름으로 전송된 파일 읽어서 myfile에 저장
    myfile = request.FILES["file"]
    #4.2 fs에 파일이 업로드 될 위치 저장
    fs = FileSystemStorage(location="media/DjangoStudy", base_url="media/DjangoStudy")
    #4.2 truename에 원본 파일 이름 저장
    truename = myfile.name
    #4.3 파일이 저장위치에 업로드 될 때 uuid가 추가된 이름으로 업로드
    #업로드 된 파일에 이름 중복을 방지하기 위하여 파일 이름에 uuid를 추가하여 저장 = 업로드 되면서 또한번 파일이름이 변경.
    filename = fs.save(truename + str(uuid.uuid1()), myfile)
    #4.4 업로드된 파일의 URL
    upload_fileurl = fs.url(filename)
    return HttpResponse("업로드 된 파일이름 : " + filename + ", url : " + upload_fileurl)

#5. 쿠키 생성/읽기 요청시, cookieCreate함수, cookieRead함수
def cookieCreate(request):
    #인스턴스 생성
    response = HttpResponse("쿠키 생성 되었다")
    #쿠키에 데이터 저장
    response.set_cookie("name", "youngjin")
    #세션에 데이터 저장
    request.session["age"] = "24"
    return response

def cookieRead(request):
    #쿠키 읽기
    name = request.COOKIES.get("name", "기본값")
    #세션 읽기
    age = request.session.get("age", "기본값")
    return HttpResponse(name + "이는 " + age + "세 입니다.")