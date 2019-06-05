
# 문제
# 지훈이는 Sort 마스터다. 
# 그래서 어떠한 N개의 원소를 가진 배열이 들어오더라도 암산으로 오름차순 정렬을 할 수 있다고 한다. 
# 의심 많은 보성이는 지훈이를 테스트해 보기로 마음먹었다. 
# 하지만 모든 원소를 일일이 다 확인하는 것은 너무 귀찮은 일이라 생각한 보성이는 
# 정렬된 배열의 마지막 원소만 맞는지 확인해 보기로 했다.
# 보성이를 위하여 마지막 원소를 알려주는 프로그램을 만들어주자.
# 
# 입력
# 첫째 줄에 N이 주어진다. (1 ≤ N ≤ 500,000)
# 다음 줄에는 N개의 정수 A[1], A[2], ... , A[N]이 주어진다. (0 ≤ A[i] ≤ 109)
# 
# 출력
# 첫째 줄에 정렬된 배열 A의 마지막 원소를 출력한다.

N = int(input())
arr = []

while len(arr) != N:
    arr.extend(list(map(int, input().split())))

print(max(arr))
