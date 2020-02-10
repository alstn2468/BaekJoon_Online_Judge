# 문제
# 어떤 사각형의 네 꼭짓점이 원과 접할 때 이 사각형이 원에 내접한다고 한다.
# 세 선분의 길이가 주어지고 그중 가장 긴 선분의 길이가 내접할 원의 지름과 같을 때,
# 나머지 한 선분의 길이를 구하여라.
#
# 입력
# 첫 번째 줄에 세 변의 길이를 나타내는 세 정수 a, b, c가 주어진다. (1 ≤ a, b, c ≤ 100)
# 세 선분은 내림차순으로 주어진다.
#
# 출력
# 첫째 줄에 나머지 한 변의 길이를 출력한다.
# 원에 내접하는 사각형을 만들 수 없다면 -1을 출력한다.
# 단, 정답은 정수로 나오는 케이스만 주어진다.

a, b, c = map(int, input().split())
check = False

for i in range(1, a):
    temp = a * i + b * c

    if temp ** 2 == ((a * a - b * b) * (a * a - c * c)):
        check = i

print(-1) if not check else print(check)
