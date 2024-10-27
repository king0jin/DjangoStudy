# DjangoStudy
파이썬 웹 프로그래밍 프레임워크인 Django를 이용하기 

## 1단계 
프로젝트와 애플리케이션 생성하기
+ 프로젝트 생성
  + **django-admin startproject 프로젝트이름 경로**
    + 내가 설정한 프로젝트이름의 디렉토리와 manage.py가 생성된다.
+ 애플리케이션 생성하기
  + **python manage.py startapp 애플리케이션이름**
    + 내가 설정한 애플리케이션이름의 디렉토리가 생성된다.
   
## 실행하기
**python manage.py runserver IP주소:포트번호**
+ 포트번호를 생략하면 **8000**번으로 자동 설정된다.
+ 로컬에서 실행하여 접속할 시 IP주소는 **127.0.0.1**이다 
  + Chrome브라우저에 **127.0.0.1:8000**으로 검색하면 django화면을 볼 수 있다.
