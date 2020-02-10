# 문제
# 시흠이는 최근에 레스토랑 "삼각형"을 오픈했고, 시흠이는 레스토랑을 상징하는 네온 사인을 주문했다.
# 네온 사인은 총 N개의 꼭짓점이 원의 둘레를 따라 찍혀져 있다.
# 그리고, 총 N * (N-1) / 2개의 야광 튜브가 꼭짓점을 연결하고 있다.
# 야광 튜브는 두 가지 색(빨간색과 파란색)이 있다.
# 시흠이는 한 번에 한 삼각형만 불을 밝히려고 한다.
# 이때, 삼각형의 모든 변은 색상이 같아야 하고, 꼭짓점이 서로 이어져 있어야 한다.
# 그는 이러한 단색 삼각형의 개수를 알려고 한다.
# 예를 들어, 아래 네온 사인에는 단색 삼각형이 두 개 있다. (1, 3, 5)와 (2, 3, 4)
# 네온 사인의 꼭짓점의 수와 각 야광 튜브의 색상이 주어졌을 때,
# 단색 삼각형의 개수를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에는 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스의 첫째 줄에는 꼭짓점의 개수 N(3 ≤ N ≤ 1,000)이 주어진다.
# 다음 N-1개의 각 야광 튜브의 색이 주어진다.
# 이 줄의 i번째 줄에는 꼭짓점 i와 연결된 튜브의 색상이
# i+1번 꼭짓점과 연결된 튜브부터 N번까지 순서대로 주어진다.
# 빨간색은 1, 파란색은 0으로 주어진다.
#
# 출력
# 각 테스트 케이스에 대해서 단색 삼각형의 개수를 출력한다.

for _ in range(int(input())):
    N = int(input())
