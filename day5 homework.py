from collections import deque

# 입력 받기
n, k = map(int, input().split())

# 1부터 n까지의 숫자를 포함하는 deque 생성
deq = deque(range(1, n + 1))

# 출력 형식 맞추기
print("<", end="")

# 제거되는 과정을 보기 위한 반복문
while len(deq) > 1:
    print(f"현재 deque 상태: {list(deq)}")  # 현재 deque 상태 출력
    deq.rotate(-(k - 1))  # 왼쪽으로 (k-1)칸 회전
    removed = deq.popleft()  # k번째 요소 제거
    print(f"제거된 요소: {removed}\n")  # 제거된 요소 출력
    print(f"제거 후 deque 상태: {list(deq)}\n")  # 제거 후 deque 상태 출력

    # 출력 형식 맞추기
    print(f"{removed}, ", end="")

# 마지막 남은 숫자 출력
print(f"{deq[0]}>")