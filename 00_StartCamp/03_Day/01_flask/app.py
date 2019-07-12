## 플라스크 시작.
from flask import Flask
import datetime        #datetime을 쓰기위해.
import random

app = Flask(__name__) # 현재는 이해하지 않아도 된다.

@app.route('/')
def hello():
    return 'Hello world!'

@app.route('/ssafy')        # 이렇게 주소에 치면 밑에 리턴문이나온다.
def ssafy():
    return 'This is ssafy!'

@app.route('/dday')
def dday():
    today = datetime.datetime.now()
    endgame = datetime.datetime(2019, 11, 29)
    td = endgame - today # 얼마만큼의 일수가 남아있는지 나올것이다.
    return f'SSAFY 1학기 종료까지 {td.days} 일 남았습니다.'

@app.route('/html')
def html():
    return '<h1>This is HTML h1 tag!</h1>'

@app.route('/html_line')
def html_line():
    return """
    <h1>여러줄로 작성하자!</h1>
    <ul>
        <li>1번</li>
        <li>2번</li>
    </ul>
    """

@app.route('/greeting/<string:name>')
def greeting(name):
    return f'반갑습니다! {name}님!' 

@app.route('/cube/<int:number>')
def mul(number):
    return f'{number}의 3제곱은 {number**3}입니다.'

# 점심 메뉴 리스트(5개)에서 2개를 뽑아 출력하기

@app.route('/lunch/<int:person>')
def menu(person):
    menu = ['짬뽕', '짜장면', '김밥', '빵', '불고기']
    random_ = random.sample(menu, person)
    return str(random_)
