# 패턴매칭

## 문자열 교체하기

* 문자열 내에서 '1, 2'라는 문자열을 'one, two'라는 문자열로 변경하는 경우

![1565762695384](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1565762695384.png)

![1565763114661](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1565763114661.png)

* 패턴매칭 알고리즘

  패턴매칭: 본문에서 특정한 문자열을 찾는것

  * 고지식한 알고리즘 (Brute Force)

    ![1565763284254](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1565763284254.png)

한칸씩 옮겨지면서 계속 비교해나가는것.

p: 찾을 패턴, t: 전체택스트 , M = len(p), N = len(t)

```C
def BruteForce(p, t):
	i = 0 // t의 인덱스
    j = 0 // p의 인덱스
    while j < M and i < N:
		if t[i] != p[j]:
			i = i-j
			j = -1
        i = i + 1
        j = j + 1
       if j == M: return i - M // 검색성공
       else: return - 1 // 검색실패
```



* 고지식한 패턴 검색 알고리즘의 시간 복잡도

  최악의 경우 시간복잡도는 텍스트의 모든 위치에서 패턴을 비교해야 하므로 O(MN)이 됨.

  길이가 