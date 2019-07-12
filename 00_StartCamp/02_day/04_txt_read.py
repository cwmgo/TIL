#1-1. 파일 읽기(옛날 방식) - read()

# f = open('ssafy.txt', 'r') 
# all_text = f.read() #개행 포함 문자열로 return 해주는 친구
# print(all_text)     #all_text라는 변수로 ssafy.txt를 조작할 수 있게 되었다.
# f.close()

#1-2. 파일 읽기(최신 방식) - read()

# with open('with_ssafy.txt', 'r') as f:
#     all_text = f.read() # .read()를 쓰면 안에있는 내용을 다가져온다고 생각해
#     print(all_text)

#2-1. 파일 읽기 (옛날 방식) - readlines()

# f = open('ssafy.txt', 'r')  #open 해서 무엇을 하고 뱉어낸 값을 f에 저장한다.
# lines = f.readlines() ## 각 라인을 리스트에 요소로 넣는다. 반환값이 리스트이다!

# for line in lines:
#     print(lines) ## 각 라인을 리스트의 요소로 넣어서 리스트로 출력함.
#     print(line)  ## 각 라인을 그냥 출력.

# f.close()

#2-2. 파일 읽기 (최신 방식) - readlines()

# with open('with_ssafy.txt', 'r') as f:
#     lines = f.readlines()
#     for line in lines:          #print 자체는 치고나면 개행을 담고있다.
#         print(line.strip())     #strip(): 제거한다는 함수. line을 제거한다.
