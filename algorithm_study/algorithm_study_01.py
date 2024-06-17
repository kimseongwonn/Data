# -*- coding: utf-8 -*-
"""알고리즘_01_빅오표기법_재귀호출.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LhmjmoN2c_jC64fYbaKcCPx0xQDPOluZ

### 알고리즘이란?

- 어떤 문제를 풀기 위한 절차나 방법
- 알고리즘은 주어진 '입력'을 '출력으로 만드는 과정
- 알고리즘의 각 단계는 구체적이고 명료해야함

> 어떤 문제는 보통 명료하지 않은 상태로 주어진다.
> 이러한 문제를 구체적이고 명료하게 구조화 시키는 것부터 출발
> 문제를 해결하는 방법은 여러가지가 될 수 있다. 따라서 여러가지 해결방법 중 가장 적합한 알고리즘을 찾는 것이 중요하다.
"""

# 절대값 구하기 알고리즘

import math # 수학 모듈 사용 : import로 불러오기

# 방법 1
def abs_sign(a): # 절대값 구하는 함수 정의 - 함수 이름 : abs_sign
    if a >= 0:
        return a
    else:
        return -a

# 방법 2
def abs_square(a):
    b = a * a
    return math.sqrt(b) # math.sqrt() : 수학 모듈의 제곱근 함수 - 결과값 실수 형식으로 출력된다

print(abs_sign(5))
print(abs_sign(-3))
print()
print(abs_square(5))
print(abs_square(-3))

"""### 첫 번째 알고리즘 기초 실습 문제 ###
- 1부터 n까지 합 구하기
- 최대값 찾기
- 동명이인 찾기

1부터 n까지 합 구하기
"""

# 1부터 n까지 합 구하기

# 입력값 : n
# 출력값 : 1부터 n까지의 합

# 알고리즘1
# 1부터 n까지 하나씩 더해주는 방법

def sum_n(n):
    s = 0
    for i in range(1,n+1): # 1부터 n까지 차례대로 i로 불러오겠다.
        s += i # s = s + i # 다음 식을 반복 : s에 1부터 n까지 차례대로 더해진다.
    return s

# 알고리즘2
# 합계를 구하는 방법을 공식화하여 {n*(n+1)}/2 를 활용하기
def sum_n2(n):
    s = (n*(n+1))//2 # // : 몫을 구하는 연산자 활용하여 정수부분만 출력해주기
    return s

print(sum_n(10))
print(sum_n(100))
print()
print(sum_n2(10))
print(sum_n2(100))

# 위의 2가지 방법 중 어떤 것이 더 적합한가 판단하여 상황에 맞는 알고리즘을 적용시키는 것이 중요함
# n의 크기에 따라 알고리즘 1의 경우 n번 만큼 for 문이 반복되어야 하지만 알고리즘 2의 경우 n의 크기에 상관 없이 수식에만 대입해주면 값이 출력됨

"""##빅오 표기법 (O 표기법)
- 알고리즘이 문제를 해결하기 위해 수행하는 계산이 얼마나 복잡한가에 따라 성능이 완전 달라진다
- 이러한 복잡도를 **계산복잡도(complexity)**라고 한다.
- 계산복잡도를 표기하는 대표적인 방법으로 O 표기법이 있다.

> O(n) : 위의 알고리즘 1 처럼 n의 크기와 계산 횟수를 특정 수식으로 나타낼 수 있으면(= 연관 관계가 발생하면) 다음과 같이 표기한다.

> O(1) : 위의 알고리즘 2처럼 n의 크기와 계산 횟수 사이에 어떠한 연관 관계도 발생하지 않으면 다음과 같이 표기한다.


---
####계산복잡도
- 시간복잡도 : 알고리즘이 수행하는데 얼마나 오랜 시간이 걸리는지에 대한 정도(연산 횟수)
- 공간복잡도 : 알고리즘이 수행하는데 얼마나 많은 공간이 필요한지에 대한 정도(메모리/ 기억장소)

"""

# 연습문제
# 1부터 n까지 제곱의 합을 구하는 프로그램

# 알고리즘 1
# 하나씩 차례대로 계산
# O(n)

def sum_sq(n):
    s = 0
    for i in range(1, n+1):
        s += i**2
    return s

print(sum_sq(10))
print(sum_sq(100))

# 알고리즘 2
# 공식 활용
# O(1)

def sum_sq2(n):
    s = n*(n+1)*(2*n+1)//6
    return s

print(sum_sq2(10))
print(sum_sq2(100))

"""최대값 찾기"""

# 최대값 찾기
# 입력값 : n개의 숫자가 들어있는 리스트
# 출력값 : 주어진 숫자 리스트 중 최대값

def max_find(a):
    n = len(a)
    max = a[0] # 최대값을 리스트 a의 첫번째 값으로 임의 지정
    for i in range(n): # len(a) > 리스트 a의 길이 즉 리스트 안에 들어있는 숫자의 개수
        if max <= a[i]: # 만약 max가 a[i] 리스트 a의 i번째 값보다 작으면 max는 a[i]이다(교체된다.)
            max = a[i]
    return max

a = [17, 92, 18, 33, 58, 7, 33, 42]
print(max_find(a))

# n(=len(a))의 크기에 따라 계산 횟수가 달라짐 >> O(n)

"""동명이인 찾기"""

# 동명이인 찾기
# n명의 사람 이름 중에서 같은 이름을 찾아 집합으로 만들어 돌려주는 알고리즘

# 입력값 : n명의 이름이 들어있는 리스트
# 출력값 : 동명이인의 이름이 들어 있는 집합

# 집합(set())은 요소값의 중복을 허용하지 않는다.

def same_name(a):
    n = len(a) # 리스트 a의 길이
    name_set = set()
    for i in range(0, n-1): # a[0]부터 a[n-2]까지 반복 >> a[n-1]은 마지막 요소이므로 반복 불필요(앞의 요소들이 반복되면서 마지막 요소는 이미 다 비교됨)
        for j in range(i+1, n): # a[i+1]부터 a[n-1]까지 반복 >> a[i]와는 앞서 이미 비교되었기 때문에 i+1부터 시작
            if a[i] == a[j]: # 이름이 동명이면
                name_set.add(a[i]) # 집합 name_set에 추가해라
    return name_set

a = ['Tom', 'Jerry', 'Mike', 'Tom']

# 첫번째 for문에서 i의 범위 >> 0~2
# i = 0부터 시작 >> a[0](Tom)이 a[1](Jerry)부터 a[3](Tom)까지 비교
# i = 1 >> a[1](Jerry)가 a[2](Mike)부터 a[3](Tom)까지 비교
# i = 2 >> a[2](Mike)가 a[3]하고 비교

print(same_name(a))

# n(len(a))의 크기에 따라 계산 횟수가 달라짐
# n = 1 일때 비교 횟수는 0회
# n = 2 일때 비교 횟수는 1회
# n = 3 일때 비교 횟수는 3회
# n = 4 일때 비교 횟수는 6회
# n = 5 일때 비교 횟수는 10회
# 즉 비교 횟수는 0부터 (n-1)까지의 합
# 비교 횟수는 ((n-1)(n-1+1))/2 = (n^2-n)/2 >> 0부터 n까지 합의 공식 활용 n대신 n-1 대입
# 따라서 위의 알고리즘의 계산복잡도는 O(n^2)으로 표현가능 >> 가장 높은 차수만 고려 & 가장 높은 차수 앞 계수는 무시



"""두 번째 알고리즘 기초 실습 문제
- 팩토리얼 구하기
- 최대공약수 구하기
- 하노이의 탑 옮기기

팩토리얼 구하기
"""

# 팩토리얼 구하기
# 1부터 n까지 연속한 정수의 곱을 구하는 알고리즘

# 입력값 : 숫자 n
# 출력값 : 1부터 n까지 곱

def fact(n):
    s = 1 # 초기화
    for i in range(1, n+1): # 1부터 n까지 범위 설정
        s *= i # s = s * i >> s에 곱한 값 누적시키기
    return s

print(fact(5))

"""###재귀 호출
- 어떤 함수 안에서 자기 자신을 다시 부르는 것
"""

# 재귀함수 예시
'''
def hello():
    print("hello")
    hello()
'''
# "hello" 라는 문장을 출력하는 함수 hello()를 함수 안에서 스스로 다시 부름
# "hello" 라는 문장을 출력한 후 자기 자신을 다시 부르므로 "hello" 라는 문장이 영원히 출력됨

# 즉, 재귀 호출 프로그램이 정상적으로 작동하려면 종료 조건이 필요하다
# 특정 조건이 되면 더는 자신을 호출하지 않도록 설계 (그렇지 않으면 재귀 에러 발생)

"""러시아 인형 마트료시카"""

# 러시아 인형 마트료시카
# 재귀 함수는 자기 자신 안에 또 자기 자신이 들어있다는 점에서 러시아 인형 마트료시카와 비슷하다

# 팩토리얼 구하기
# 재귀 함수 사용

def fact2(n):
    if n <= 1: # fact2(1)에 도달하는 순간 n은 1보다 작거나 같아지는 조건이 만족되므로 더 이상 자신을 호출하지 않고 1을 반환
        return 1
    return n*fact2(n-1) # fact(n-1)이 계속해서 출력되다보면 fact2(1)에 도달하게 됨

print(fact2(1))
print(fact2(5))

# fact2(4) = 4 * fact2(3)
# fact2(3) = 3 * fact2(2)
# fact2(2) = 2 * fact2(1)
# fact2(1) = 1
# 따라서 fact2(4)는 4*3*2*1의 값이 리턴된다.

"""####재귀호출의 일반적인 형태"""

'''
def 함수이름(입력값):
    if 입력값이 충분히 작으면: # 종료조건
        return 종료 조건을 충족한 결과값
    함수이름(더 작은 입력값) # 입력값 감소시키면서 자신 호출 >> 입력값이 충분히 작아져서 종료 조건을 만족시켜야 하기 때문
    return 결과값
'''

# 재귀 호출 연습 문제 1
# 1부터 n까지의 합 구하는 알고리즘을 재귀 호출로 만들기

def sum(n):
    if n == 1:
        return 1
    return n + sum(n-1)

print(sum(10))

# 재귀 호출 연습 문제 2
# 숫자 n개 중에서 최대값 찾기를 재귀호출로 만들기

def find_max(a, n): # n개의 요소를 가진 리스트 a의 최댓값을 구하는 재귀 함수
    if n == 1: # 만약 요소가 1개면 최대값은 당연히 a[0] >> n이 1에 도달하면 멈추는 종료 조건
        return a[0]
    max_n_1 = find_max(a, n - 1) # n-1개 중 최댓값 >> n의 값이 감소되면서 결국 1에 도달
    if max_n_1 > a[n - 1]:  # n-1개 중 최댓값과 n-1번 위치 값을 비교
                            # n-1 해주는 이유는 인덱스는 0부터 시작하므로 n번째 요소의 인덱스는 n-1
                            # 즉, a[n-1]은 가장 마지막 요소
                            # 따라서 마지막 요소부터 하나씩 비교하는 재귀 함수가 된다.
        return max_n_1
    else:
        return a[n - 1]

a = [17, 92, 18, 33, 58, 7, 33, 42]
# n = len(a) = 8
print(find_max(a, len(a)))
