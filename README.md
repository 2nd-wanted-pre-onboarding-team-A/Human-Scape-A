## 👩‍💻 Team

- **[양수영](https://github.com/tasddc1226)**
- **[권은경](https://github.com/fore0919)**
- **[윤상민](https://github.com/redtea89)**

```
프로젝트 진행 기간 2022.05.10 09:00 ~ 2022.05.13 18:00
```

[`Team-A-notion`](https://pretty-marlin-13a.notion.site/Team-A-03cf51c7174847ce88a6302e6939ea2a)



## 개인별 구현방법 및 어려웠던 점

- 양수경

  - .
  - .

  

- 권은경

  - .
  - .

  

- 윤상민

  - .
  - .



## 프로그램 실행방법

로컬환경에서 이 프로그램을 실행시키려면 Django SECRET_KEY와 API KEY이 필요하다. 이 실행방법은 KEY를 알고 있다는 가정하에 작성되었다. 



> ###### MAC OS



###### 1번. 터미널에에서 프로그램을 내려받을 폴더로 이동한다.  (Documents 디렉터리 예시)

```bash
% cd ~/Documents
```



###### 2번. git clone으로 파일을 받고 프로젝트 폴더로 이동한다. 

```bash
% git clone https://github.com/2nd-wanted-pre-onboarding-team-A/Human-Scape-A.git
```

```bash
% cd Human-Scape-A
```



###### 3번. 폴더 트리 확인

```bash
% ls

# 예시 화면
README.md		human			requirements.txt
__pycache__		manage.py		research
core			dockerfile		paper
```

앞으로 이 디렉터리의 상태를 "프로젝트 폴더"라 부르겠다. 



###### 4번. 파이썬 설치 확인

```bash
% python --version

# 예시화면
Python 3.8.10
```

만약 파이썬 3.8이상이 설치되어있지 않다면 [링크](https://www.python.org/downloads/) 로 이동하여 파이썬 3.8.10 (혹은 3.8.12) 를 설치한다. 



###### 5번. (파이썬 설치가 완료되었다면 3번 폴더 위치에서) 가상환경 생성

```bash
% python -m venv venv
```



###### 6번. 가상환경 진입

```bash
% source venv/bin/activate
```



###### 7번. 파이썬 모듈 설치

```bash
% pip install --upgrade pip
% pip install -r requirements.txt
```

여기서 에러가 난다면 3번부터 정상적으로 되었는지 확인하여야 한다. 



###### 8번. 환경변수 파일 만들기

프로젝트 폴더에서 파일명 my_settings.py를 만들고 아래의 내용을 붙여넣기한다. (KEY 내용은 이미 알고 있는 내용을 집어넣으면 된다.)

```python
# my_settings.py

DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'human',
        'USER': 'root',
        'PASSWORD': 'mysecretpassword',
        'HOST': 'localhost',
        'PORT': '3306',
		'OPTIONS': {'charset': 'utf8mb4'}
    }
}

SECRET_KEY = ''
DEBUG = True

OPEN_API_SECRET_KEY = ''
OPEN_API_SECRET_KEY_CHALLENGE = ''
```



###### 9번. 로컬 환경에 Mysql 설치

이미 Mysql이 설치되어있다면 이 과정은 넘어가도 된다. 만약 brew가 설치되어 있지 않다면 [이곳](https://brew.sh/index_ko)을 참고 

```bash
% brew install mysql
% brew services start mysql
```

루트 비밀번호 세팅 (이곳 비밀번호가 8번 환경변수 파일 만들기의 비밀번호에 들어가야한다.)

```bash
% mysqladmin -u root password 'mysecretpassword'
```

터미널에서 mysql 접속확인(터미널 아무위치에서해도 상관없음)

```bash
% mysql -u root -p
% mysecretpassword
```



###### 10번. database 생성

mysql에 접속하였다면 터미널 명령창이 아래와 같이 mysql> 로 바뀐다. 

```mysql
mysql> create database human character set utf8mb4 collate utf8mb4_general_ci;
```



###### 11번. Django를 이용한 Mysql DB 테이블 생성

프로젝트 폴더(3번 참고)로 이동하여 아래와 같이 입력

```bash
% python manage.py migrate
```



###### 12번. Django 서버 실행

프로젝트 폴더에서 아래의 명령어를 입력한다. 

```bash
% python manage.py runserver --noreload
```



###### 13번. 로컬 API테스트

터미널에서 아래의 명령어를 입력한다. 

```
curl
```



---



## API Documentation







