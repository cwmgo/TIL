#1. 각각의 라인을 리스트의 요소로 불러오기
with open('writelines_ssafy.txt', 'r') as f:
    lines = f.readlines()

#2. 뒤집기
lines.reverse()     # sort는 method, sorted 는 함수 reverse()는 원본을 바꾸는것.
                             # sorted: 리턴하는애들은 원본을 그대로 두고 새롭게 리턴하는것.
                             # sort는 원본을 정렬해버리는것. 함수가 큰개념이고 메서드가 그안에 들어가있다.
                             # 클래스 안에 정의된 함수를 메서드라고 한다.
#3. line을 작성하기
with open('reverse_ssafy.txt', 'w') as f:
    for line in lines:
        f.write(line)