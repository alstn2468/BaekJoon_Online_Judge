# 문제
# 두 문자열 A와 B가 주어졌을 때,
# A에 연산을 최소 횟수로 수행해 B로 만드는 문제를 "최소 편집" 문제라고 한다.
# A에 적용할 수 있는 연산은 총 3가지가 있으며 아래와 같다.
# 삽입: A의 한 위치에 문자 하나를 삽입한다.
# 삭제: A의 문자 하나를 삭제한다.
# 교체: A의 문자 하나를 다른 문자로 교체한다.
# 두 문자열이 주어졌을 때, 최소 편집 횟수를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄과 둘째 줄에 두 문자열이 주어진다.
# 문자열은 알파벳 소문자로만 이루어져 있으며, 최대 1000글자로 이루어져 있다.
#
# 출력
# 첫째 줄에 최소 편집 횟수를 출력한다.

import sys

sys.setrecursionlimit(987654321)

dist = [[0 for _ in range(1001)] for _ in range(1001)]
A = input()
B = input()


def solution(indexA, indexB):
    if indexA >= len(A) and indexB < len(B):
        return len(B[indexB:])

    elif indexB >= len(B):
        return len(A[indexA:])

    if dist[indexA][indexB] != 0:
        return dist[indexA][indexB]

    if A[indexA] == B[indexB]:
        dist[indexA][indexB] = solution(indexA + 1, indexB + 1)

    else:
        dist[indexA][indexB] = 1 + min(
            solution(indexA + 1, indexB),
            solution(indexA, indexB + 1),
            solution(indexA + 1, indexB + 1),
        )

    return dist[indexA][indexB]


print(solution(0, 0))
