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
---
## settings.py
### 프로젝트 설정 파일
secret key, debug mode, 개발환경에서 수행되는 내용을 다르게 만들고 할 때 등등의 설정을 할 수 있다
+ DEBUG
  + True : 개발 모드
  + False : 운영 모드
+ ALLOWED_HOSTS
  + 운영 모드인 경우 : 반드시 서버의 IP/도메인을 기재
  + 개발 모드인 경우 : 자동으로 localhost, 127.0.0.1로 간주
    + 모든 컴퓨터 : '*'
+ INSTAKKED_APPS
  + 사용할 패키지와 애플리케이션 기재
+ MIDDLEWARE
  + 요청이 오기 전/후에 수행할 내용을 기재
+ DATABASE
  + 기본으로 sqlite3로 설정되어 있다
---
## 관리자 계정
django는 데이터베이스 관리 기능을 편리하게 하기위해서 관리자 사이트를 별도로 제공한다
+ 웹브라우저에서 기본URL/admin으로 접속하면 로그인화면을 볼 수 있다
  + ex) http://127.0.0.1:8000/admin
처음에는 계정이 존재하지않으므로 데이터베이스 연결을 수행하면서 관리자 계정을 생성해야한다

### 데이터베이스 연결
장고 프로젝트를 처음 실행하기 전이나 데이터베이스에 변경 사항이 있는 경우 데이터베이스 설정을 다시 해달라고 요청을 할 수 있다
1. python manage.py migrations
2. python manage.py migrate

### 관리자 계정 생성
**python managy.py createsuperuser**
명령을 수행하고 이름, 이메일, 비밀번호를 입력하여 계정을 생성한다 
