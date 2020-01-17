# Django_Study

- 개발환경
1. python 3.7
2. Django 3.0.2

- 참고사이트
1. https://docs.djangoproject.com/ko/3.0/intro/tutorial01/ : Django 3.0 듀토리얼

- 참고 명령어
    - python - django --version : django 버전 확인
    - django-admin startproject {프로젝트명} : django 프로젝트 생성
    - python manage.py runserver : 서버 실행(manage.py가 존재하는 디렉토리에서 입력)
        - 기본적으로 8000포트 개발 서버를 띄우는데 runserver {포트} 를 이용하면 원하는 포트로 서버 실행
    - python manage.py startapp {앱명} : 최상위에서 곧바로 임포트 가능한 기본 앱 생성
    - python manage.py createsuperuser : 관리 사이트 생성하기
    - python manage.py shell : 파이썬 쉘 스크립트 사용
    
    - python manage.py migrate : INSTALLED_APPS의 세팅과 일치하는 데이터베이스 테이블을 만든다.
    - python manage.py makemigrations polls : polls앱의 모델이 변경 또는 새롭게 만들어진것을 migration에 저장한다.
    - python manage.py sqlmigrate polls 0001 : migration의 이름을 인수로 받아 실행하는 SQL문장을 보여줌
    
- 관리자 사이트
    - id : admin