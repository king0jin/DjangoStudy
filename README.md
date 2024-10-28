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

---
## 요청 URL과 처리 함수
+ 요청 URL : urls.py
+ 처리함수 : views.py
  + 간단한 내용을 HTML로 출력 : HttpResponse객체에 직접 내용 작성
  + 복잡한 내용(서버가 처리하고 전달받은 데이터)을 출력 : **template**
 
### template
규격에 맞게 작성하면 HTML로 변환하여 서버가 클라이언트에게 전송
+ 애플리케이션 디렉토리에 templates디렉토리 생성
  + views.py에서 함수의 리턴 값으로 render()를 리턴한다
    + render의 매개변수
      1. 클라이언트가 전달한 request
      2. 최종적으로 출력하는 파일의 경로 ex) index.html
      3. 템플릿으로 전달되는 데이터(키:값 형태) ex) {'키':"값"}
     
#### index.html
body 태그 안 {{ }} : Django의 템플릿에서 {{ 키 }}는 해당 키의 값이 그 자리로 치환된다.

### URL에 포함된 데이터 처리
요청경로/<자료형:데이터이름>
+ 요청 처리 함수에 데이터이름을 매개변수로 지정

---
## GET - queryString처리
URL에 파라미터(키)를 포함하여 데이터를 요청하는 메서드
+ 브라우저에서 바로 테스트 가능
  + **querystring/?키=값** 형태
+ 보안성이 낮다
+ 데이터 길이에 제한이 있다
+ 처리 함수에 기본값 설정을 해줘야 한다
