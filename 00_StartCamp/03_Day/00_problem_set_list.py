"""
문자열을 입력받아 문자열의 첫 글자와 마지막 글자를 출력하는 프로그램을 작성하시오.
"""
# strinput = input("문자열을 입력하시오\n")
# print("{0}, {1}".format(strinput[0], strinput[len(strinput)-1]))
# #print(f'첫 글자는 {str[0]}')
# #print(f'마지막 글자는 {str[-1]}입니다.')

"""
문제2. 자연수 n이 주어질 때, 1부터 n까지 한 줄에 하나씩 출력하는 프로그램을 만드세요.
"""
# n = int(input("자연수를 입력하세요: "))
# if n > 0:
#     for i in range(0, n):
#         print(f'{i+1}')
# else:
#     print(f'잘못된 입력입니다.')

"""
문제3. 숫자를 입력 받아 짝수/ 홀수를 구분하는 코드를 작성하세요.
"""

# number = int(input('숫자를 입력하세요: '))
# if number% 2 == 0 :
#     print("짝수 입니다.")
# else:
#     print("홀수 입니다.")

"""
문제4. 표준 입력으로 국어, 영어, 수학, 과학 점수가 입력됩니다.
국어는 90점 이상,
영어는 80점 초과,
수학은 85점 초과,
과학은 80점 이상일 때 합격이라고 정했습니다.
(한 과목이라도 조건에 만족하지 않으면 불합격)
다음 코드를 완성하여 합격이면 True, 불합격이면 False가 출력되도록 작성하세요.
"""

# a = int(input('국어: '))
# b = int(input('영어: '))
# c = int(input('수학: '))
# d = int(input('과학: '))

# if a >= 90:
#     if b > 80:
#         if c > 85:
#             if d >= 80:
#                 print("True")
#             else:
#                 print("False")
#         else:
#             print("False")
#     else:
#         print("False")
# else:
#     print("False")

#if a >= 90 and b > 80 and c > 85 and d >= 80:
#   print(True)
#else:
#   print(False)

"""
문제5. 표준 입력으로 물품 가격 여러 개가 문자열 한 줄로 입력되고, 각 가격은
; (세미콜론)으로 구분되어 있습니다. 입력된 가격을 높은 가격순으로 한줄에
하나씩 출력하는 프로그램을 만드세요.
입력예시: 30000;2000;40000
출력예시
40000
30000
2000
"""
# prices = input('물품 가격을 입력하세요: ')
# list = prices.split(';')

# for i in range(0, len(list)-1):
#     if int(list[i]) >= int(list[i+1]):
#         temp = int(list[i+1])
#         list[i+1] = int(list[i])
#         list[i] = temp

# for i in range(0, len(list)):
#     print('{0}'.format(list[i]))

# prices = input('물품 가격을 입력하세요')

# makes = prices.split(';')
# boxs = []
# # print(makes)
# # print(type(makes))
# for make in makes:
#     boxs.append(int(make))

# boxs.sort(reverse=True)

# for box in boxs:
#     print(box)
