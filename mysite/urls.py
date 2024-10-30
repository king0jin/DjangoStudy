"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

#myweb애플리케이션에 있는 views.py내용 가져오기
from myweb import views

urlpatterns = [
    #admin요청이 왔을 때, admin.site에 있는 urls함수 호출
    path('admin/', admin.site.urls),
    #1. 기본 요청 설정
    path('', views.index), #myweb.views에 있는 index함수 호출
    #2. 문자열 형태의 get 요청 설정
    path('get/<str:itemid>', views.getItem), #myweb.views에 있는 getItem함수 호출
    #2.1 문자열 형태의 get 요청시, 쿼리 적용
    path('querystring/', views.queryString), #myweb.views에 있는 queryString함수 호출
    #3. Post요청
    path('requestbody', views.requestBody), #myweb.views에 있는 requestBody함수 호출
    path('formdata', views.formData), #myweb.views에 있는 formData함수 호출
    #4. 파일 업로드 요청
    path('fileupload', views.fileUpload), #myweb.views에 있는 fileUpload함수 호출
    #5. 쿠키 생성/읽기 요청
    path('cookiecreate', views.cookieCreate), #myweb.views에 있는 cookieCreate함수 호출
    path('cookieread', views.cookieRead), #myweb.views에 있는 cookieRead함수 호출
    #7. 상품ID값 형태로의 해당 상품 정보 요청
    path('detail/<int:itemid>', views.detail, name='item-detail'), #myweb.views에 있는 detail함수
]
