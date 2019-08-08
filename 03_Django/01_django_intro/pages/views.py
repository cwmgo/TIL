from django.shortcuts import render
from datetime import datetime
import random
import requests

# Create your views here.
# mtv중 V에 해당하는. 굉장히 중요하다. 대부분의 로직을 다 작성하는 부분.
# url.py, models.py등등 다연결시키는파트.
# flask를 heavy하게 짜다보면 django처럼 나뉘게 된다.
# 기본적으로 app이 만들어지면 출생신고를 해야한다. 그것을 manage.py에 한다!

#1. 기본 로직
def index(request):
    return render(request, 'pages/index.html') 
    #return 에는 render! 이게 가장 기본 골격이다.
    #요청이오면 index.html을 앱아래에서 templates폴더안에서 찾는다.

def introduce(request):
    return render(request, 'pages/introduce.html')

def image(request):
    return render(request, 'pages/image.html')

#2. Template Variable(템플릿 변수)
def dinner(request):
    menu = ['족발', '햄버거', '치킨', '초밥']
    pick = random.choice(menu)
    context = {'pick': pick}
    return render(request, 'pages/dinner.html', context) #render의 3번째 인자는 반드시 딕셔너리여야한다.

#3. Variable Routing(동적 라우팅)
def hello(request, name, age):
    # names = ['justin', 'john', 'jason', 'juan', 'zzulu']
    # name = random.choice(names)
    menu = ['족발', '햄버거', '치킨', '초밥']
    pick = random.choice(menu)
    context = {
        'name': name,
        'age': age,
        'pick': pick,
    }
    return render(request, 'pages/hello.html', context)

#4. 실습
#4-1. 동적 라우팅을 활용해서(name과 age를 인자로 받아) 자기소개 페이지
def intro(request, name, age):
    context = {
        'name': name,
        'age': age,
    }
    return render(request, 'pages/intro.html', context)

#4-2. 두개의 숫자를 인자로 받아(num1, num2) 곱셈 결과를 출력.
def mux(request, num1, num2):
    result = num1*num2
    context = {
        'num1': num1,
        'num2': num2,
        'result' : result,
    }
    return render(request, 'pages/mux.html', context)

#4-3. 반지름을 인자로 받아 원의 넓이를 구하시오.
def area(request, r):
    result = round(3.14*r*r,2)
    context = {
        'r' : r,
        'result': result,
    }
    return render(request, 'pages/area.html', context)

#5. DTL(Django Template)
def template_language(request):
    menus = ['짜장면', '탕수육', '짬뽕', '양장피']
    my_sentence = 'Life is short, you need python'
    messages = ['apple', 'banana', 'cucumber', 'mango']
    datetimenow = datetime.now()
    empty_list = []

    context = {
        'menus': menus,
        'my_sentence': my_sentence,
        'messages': messages,
        'empty_list': empty_list,
        'datetimenow': datetimenow,
    }
    return render(request, 'pages/template_language.html', context)

def info(request):
    return render(request, 'pages/info.html')

#6. 실습
#6-1. isbirth
def isbirth(request):
    today = datetime.now()
    if today.month == 4 and today.day == 1:
        result = True
    else:
        result = False

    context ={
        'result': result,
    }
    
    return render(request, 'pages/isbirth.html', context )

def ispal(request, character):
    inp = list(character)
    if inp == inp[::-1]:
        result = True
    else:
        result = False
    
    context = {
        'result': result,
    }

    return render(request, 'pages/ispal.html', context )


def lottos(request):
    lottos = sorted(random.sample(range(1, 46), 6))
    real_lottos = [21, 24, 30, 32, 40, 42]
    context = {
        'lottos': lottos,
        'real_lottos': real_lottos,
    }

    return render(request, 'pages/lottos.html', context)

#7. Form - GET
#GET은 데이터에 대한 조회를 요청하는것.
#네이버에 검색을 하는것은 html 파일 한장을 줘.
#데이터에대한 조작을 하는게 아니라 server에 있는 data를 달라는 요청이 GET이다.

def throw(request):
    return render(request, 'pages/throw.html')

def catch(request):
    message = request.GET.get('message') # 이요청이 GET요청이고 데이터는 query dict형식으로 들어온다.
    message2 = request.GET.get('message2')
    context = {
        'message': message,
        'message2': message2,
    }
    return render(request, 'pages/catch.html', context)

def ping(request):
    return render(request, 'pages/ping.html')

def pong(request):
    message = request.GET.get('message')
    context = {
        'message': message,
    }
    return render(request, 'pages/pong.html', context)

#8. Form - GET(실습)(아스키 아티)
def art(request):
    return render(request, 'pages/art.html')

def result(request):
    #1. form으로 날린 데이터를 받는다.(GET)
    word = request.GET.get('word')

    #2. ARTII api로 요청을 보내 응답 결과를 fonts에 저장.
    fonts = requests.get('http://artii.herokuapp.com/fonts_list').text

    #3. fonts(str)를 fonts(list)로 바꾼다.
    fonts = fonts.split('\n')

    #4. fonts(list)안에 들어있는 요소 중 하나를 선택해서
    # font라는 변수에 저장(str)
    font = random.choice(fonts)

    #5. 위에서 사용자에게 받은 word와 font를 가지고 다시 
    # 요청을 보낸다. 그리고 응답 결과를 result에 저장한다.
    result = requests.get(f'http://artii.herokuapp.com/make?text={word}&font={font}').text
    context = {
        'result': result
    }
    return render(request, 'pages/result.html', context)

#9. Form - POST
def user_new(request):
    return render(request, 'pages/user_new.html')

def user_create(request):
    name = request.POST.get('name')
    pwd = request.POST.get('pwd')
    context = {
        'name': name,
        'password': pwd,
    }
    return render(request, 'pages/user_create.html', context)

# 14_workshop    
def push(request):
    return render(request,'pages/push.html')

def pull(request):
    num = request.GET.get('num')
    context = {
        'num': num
    }
    return render(request, 'pages/pull.html', context)

#10. 정적 파일
def static_example(request):
    return render(request, 'pages/static_example.html')

def one(request):
    return render(request, 'pages/one.html')
        