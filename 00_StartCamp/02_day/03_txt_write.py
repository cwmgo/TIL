#1. 파일 쓰기(옛날 방식)

# f = open('ssafy.txt', 'w')
# for i in range(10):
#     f.write(f'This is line {i}.\n')
# f.close()

#2. 파일 쓰기(최신 방식)

with open('with _ssafy.txt', 'w') as f: # f = open('ssafy.txt', 'w') 같은역할.
    for i in range(10):
        f.write(f'This is line {i}.\n')
        #close 할 필요가 없다. 