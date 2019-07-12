#1. 파일 쓰기(옛날 방식)

# f = open('ssafy.txt', 'w')
# for i in range(10):
#     f.write(f'This is line {i}.\n')
# f.close()

#2. 파일 쓰기(최신 방식)

# with open('with _ssafy.txt', 'w') as f: # f = open('ssafy.txt', 'w') 같은역할.
#     for i in range(10):
#         f.write(f'This is line {i}.\n')
#         #close 할 필요가 없다. 

#2-2. 파일 쓰기 (최신방식)

with open('writelines_ssafy.txt', 'w') as f:
    f.writelines(['0\n', '1\n', '2\n', '3\n'])  ##list가 안에 들어가는데 이 요소를 가지고 내용을 쓰는것
                                                ##기본적으로 개행을 안해주기 떄문에 이함수를 출력한것.
    