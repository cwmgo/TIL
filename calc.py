def plus(num1, num2):
    return num1+num2

def minus(num1, num2):
    return num1-num2

def mux(num1, num2):
    return num1*num2

def divide(num1, num2):
    try:
        return num1/num2
    except TypeError:
        print(f'\'0\'으로 나누려고 하는 경우에는 문자열 \'0\'으로는 나눌 수 없습니다.')