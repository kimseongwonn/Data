# -*- coding: utf-8 -*-
"""python_practice_008.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17v9MZOaxNFLB_QWE4DUXGSQH0T9Cb2Up

두 정수 a, b와 boolean 변수 flag가 매개변수로 주어질 때, flag가 true면 a + b를 false면 a - b를 return 하는 solution 함수를 작성해 주세요.

제한사항
- -1,000 ≤ a, b ≤ 1,000

입출력 예

1번
- a : -4
- b : 7
- flag : true
- result : 3


2번
- a : -4
- b : 3
- flag : false
- result : -11
"""

def solution(a, b, flag):

    answer = 0

    if flag:
        answer = a + b
    else:
        answer = a - b

    return answer

print(solution(-4, 7, True))
print(solution(-4, 7, False))

# 람다식 활용

solution = lambda a,b,flag:a+b if flag else a-b
# a, b, flag 라는 3개의 인자를 받아드리고 만약 flag가 참이면 a+b를 아니면 a-b를 반환한다.
# 람다식 정리
# add = lambda a, b : a+b >> add(a, b)는 a+b를 반환한다.

print(solution(-4, 7, True))
print(solution(-4, 7, False))

"""문자열 code가 주어집니다.

code를 앞에서부터 읽으면서 만약 문자가 "1"이면 mode를 바꿉니다.

mode에 따라 code를 읽어가면서 문자열 ret을 만들어냅니다.

mode는 0과 1이 있으며, idx를 0 부터 code의 길이 - 1 까지 1씩 키워나가면서 code[idx]의 값에 따라 다음과 같이 행동합니다.

- mode가 0일 때
    - code[idx]가 "1"이 아니면 idx가 짝수일 때만 ret의 맨 뒤에 code[idx]를 추가합니다.
    - code[idx]가 "1"이면 mode를 0에서 1로 바꿉니다.
- mode가 1일 때
    - code[idx]가 "1"이 아니면 idx가 홀수일 때만 ret의 맨 뒤에 code[idx]를 추가합니다.
    - code[idx]가 "1"이면 mode를 1에서 0으로 바꿉니다.

문자열 code를 통해 만들어진 문자열 ret를 return 하는 solution 함수를 완성해 주세요.

단, 시작할 때 mode는 0이며, return 하려는 ret가 만약 빈 문자열이라면 대신 "EMPTY"를 return 합니다.

제한사항
- 1 ≤ code의 길이 ≤ 100,000
    - code는 알파벳 소문자 또는 "1"로 이루어진 문자열입니다.

입출력 예
- code : "abc1abc1abc"
- result : "acbac"
"""

def solution(code):
    ret = ""
    mode = 0

    for i in range(len(code)):
        if mode == 0:
            if code[i] != "1":
                if i % 2 == 0:
                    ret += code[i]
            else:
                mode = 1
                continue
        if mode == 1:
            if code[i] != "1":
                if i % 2 == 1:
                    ret += code[i]
            else:
                mode = 0

        if len(ret) == 0:
            return "EMPTY"

    return ret

print(solution("abc1abc1abc"))

# 말문이 막히는 다른 답변...

def solution(code):
    return "".join(code.split("1"))[::2] or "EMPTY"
    # code라는 문자열을 '1'이라는 구분자로 나눠준 다음 ""로 붙여주는데 처음부터 끝까지 2의 간격으로 붙여줘

print(solution("abc1abc1abc"))

# 다른 답변
# 내 코드보다 더 간결하고 좋은 것 같다.
# 내 코드의 경우 모드를 확인하고 > code[i]값을 확인하고 > i의 홀짝 여부를 판단하여 ret에 문자를 추가하는 구조 라면
# 이 코드는 먼저 code[i]값을 확인하여 1이면 모드를 바꾸고 아니면 다음 조건으로 넘어가서 모드별 i의 홀짝 여부를 구분해주고 있다.
# 내 코드보다 더 구조적으로 효율적인 코드인것 같다

def solution(code):
    ret = ""
    mode = 0

    for i in range(len(code)):
        if code[i] == "1":
            mode = 1 - mode

        else:
            if mode == 0 and i % 2 == 0:
                ret += code[i]
            elif mode == 1 and i % 2 == 1:
                ret += code[i]

    if len(ret) == 0:
        return "EMPTY"

    else:
        return ret