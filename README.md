# Network 다이어그램
- 인터넷
  - NginX
    - /api -> Django 백엔드
    - /    -> React 프론트엔드

# Django 초기설정
1. Pycharm 을 통해서 Python3.7을 설치 후 Virtual Environment를 만듭니다.
2. Virtual Environment 에 requirement.txt에서 요구하는 라이브러리를 설치합니다.

# Django 명령어 들
|명령어|설명|
|---|---|
|`python manage.py runserver 127.0.0.1:8000`|`127.0.0.0.1:8000`에 장고를 실행합니다.|
|`python manage.py migrate`|마이그레이션을 적용합니다|
|`python manage.py makemigrations`|마이그레이션을 생성합니다.|
|`python manage.py squashmigrations`|마이그레이션을 압축합니다.|